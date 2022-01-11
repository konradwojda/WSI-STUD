import numpy as np
import gym
import random

from multiprocessing.pool import Pool

from itertools import repeat

from statistics import mean

environment = gym.make("FrozenLake8x8-v1")


def q_learning(qtable: np.array, episodes: int, max_steps: int, learning_rate: float, epsilon: float, min_epsilon: float, max_epsilon: float, decay_rate: float, gamma: float):

    success_count = 0

    for episode in range(episodes):
        state = environment.reset()
        done = False

        for step in range(max_steps):
            # Choose action
            tradeoff = random.uniform(0, 1)

            if tradeoff > epsilon:
                action = np.argmax(qtable[state, :])
            else:
                action = environment.action_space.sample()

            new_state, reward, done, info = environment.step(action)

            # Update Q table

            qtable[state, action] = qtable[state, action] + learning_rate * \
                (reward + gamma *
                 np.max(qtable[new_state, :]) - qtable[state, action])

            state = new_state

            if done:
                if reward == 1.0:
                    success_count += 1
                break

        epsilon = min_epsilon + (max_epsilon - min_epsilon) * \
            np.exp(-decay_rate * episode)

    return qtable, success_count

def learn_and_test(episodes):
    # Number of tries
    # episodes = 1000

    # Learning rate
    learning_rate = 0.8

    # Max steps per try
    max_steps = 400

    # Discounting rate
    gamma = 0.9

    # Exploration rate
    epsilon = 1.0

    # Exploration probability at start
    max_epsilon = 1.0

    # Minimum exploration probability
    min_epsilon = 0.001

    # Decay rate for exploration prob
    decay_rate = 0.00005

    qtable = np.zeros((environment.observation_space.n,
                    environment.action_space.n))

    learned_qtable, success_count = q_learning(qtable, episodes, max_steps, learning_rate, epsilon, min_epsilon, max_epsilon, decay_rate, gamma)

    environment.reset()

    test_success_count = 0

    for episode in range(1000):
        state = environment.reset()

        done = False

        for step in range(200):
            action = np.argmax(qtable[state, :])

            new_state, reward, done, info = environment.step(action)

            if done:

                if reward == 1.0:
                    test_success_count += 1

                break

            state = new_state

    environment.close()

    return test_success_count/1000

if __name__ == "__main__":

    results = []

    with Pool() as p:
        #Start testing
        for episodes in [1000, 5000, 10000, 50000, 100000, 250000]:
                success_rates = p.imap_unordered(learn_and_test, repeat(episodes, 10))

                avg_success_rate = mean(success_rates)

                results.append((avg_success_rate, episodes))

    for sr, ep in results:
        print("Nr of episodes: " + str(ep))
        print("Avg success rate: " + f'{(sr * 100):.6f}' + "%")