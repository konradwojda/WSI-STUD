import random
from typing import Counter

class Node:
    def __init__(self, name, dependents=None, prob_dict=None):
        self.name = name
        self.dependents = dependents if dependents else set()
        self.prob_dict = prob_dict if prob_dict else dict()


def generate_sample(nodes):
    sample = dict()

    for node in nodes:
        if not node.dependents:
            sample[node.name] = random.uniform(0, 1) < node.prob_dict[True]
        else:
            active_dependents = [n for n in node.dependents if sample[n]]
            idx_list = []
            for active in active_dependents:
                idx_list.append(node.dependents.index(active))
            active_list = []
            for d in range(len(node.dependents)):
                if d in idx_list:
                    active_list.append(True)
                else:
                    active_list.append(False)
            sample[node.name] = random.uniform(0, 1) < node.prob_dict[tuple(active_list)]

    return sample


if __name__ == "__main__":
    nodes = [
        Node("Chair", prob_dict={True: 0.8}),
        Node("Sport", prob_dict={True: 0.02}),
        Node("Back", dependents=["Chair", "Sport"], prob_dict={
            (True, True): 0.9,
            (True, False): 0.2,
            (False, True): 0.9,
            (False, False): 0.01
        }),
        Node("Ache", dependents=["Back"], prob_dict={(True,): 0.7, (False,): 0.1})
    ]

    samples = [generate_sample(nodes) for _ in range(100)]
    for sample in samples:
        print(sample)


