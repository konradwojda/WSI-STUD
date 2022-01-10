import numpy as np
import gym
import random

environment = gym.make("FrozenLake-v1")


def q_learning(qtable: np.array, episodes: int, max_steps: int, learning_rate: float, epsilon: float, min_epsilon: float, max_epsilon: float, decay_rate: float, gamma: float):
    rewards = []

    for episode in range(episodes):
        state = environment.reset()
        step = 0
        done = False
        rewards_count = 0

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

            rewards_count += reward

            state = new_state

            if done:
                break

        epsilon = min_epsilon + (max_epsilon - min_epsilon) * \
            np.exp(-decay_rate * episode)

        rewards.append(rewards_count)

    return qtable, rewards


if __name__ == "__main__":

    # Number of tries
    episodes = 15000

    # Learning rate
    learning_rate = 0.8

    # Max steps per try
    max_steps = 200

    # Discounting rate
    gamma = 0.95

    # Exploration rate
    epsilon = 1.0

    # Exploration probability at start
    max_epsilon = 1.0

    # Minimum exploration probability
    min_epsilon = 0.01

    # Decay rate for exploration prob
    decay_rate = 0.005

    qtable = np.zeros((environment.observation_space.n,
                      environment.action_space.n))

    learned_qtable, rewards_after = q_learning(qtable, episodes, max_steps, learning_rate, epsilon, min_epsilon, max_epsilon, decay_rate, gamma)

    print(str(sum(rewards_after)/episodes * 100) + "%")

    print(learned_qtable)

    # environment.reset()

    # for episode in range(5):
    #     state = environment.reset()

    #     step = 0

    #     done = False

    #     print("*" * 20)

    #     print(f'EP: {episode}')

    #     for step in range(max_steps):
    #         action = np.argmax(qtable[state, :])

    #         new_state, reward, done, info = environment.step(action)

    #         if done:
    #             environment.render()

    #             print(f'Number of steps: {step}')

    #             break

    #         state = new_state

    # environment.close()