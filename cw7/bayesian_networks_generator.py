import json
import random
from typing import Counter

class Node:
    def __init__(self, name, dependents=None, prob_dict=None):
        self.name = name
        self.dependents = dependents if dependents else set()
        self.prob_dict = prob_dict if prob_dict else dict()


def load_from_json(path):
    with open(path, 'r') as fh:
        data = json.load(fh)
    nodes = []
    for item in data:
        name = item["name"]
        dependents = item["dependents"]
        probabilities = item["prob_dict"]
        prob_dict = {}
        if len(probabilities) == 1:
            key = True if list(probabilities.keys())[0] else False
            prob_dict[key] = list(probabilities.values())[0]
        else:
            for booleans_str, prob in probabilities.items():
                booleans_str = booleans_str.strip(',')
                values = booleans_str.split(", ")
                booleans = []
                for elem in values:
                    if elem == 'True':
                        booleans.append(True)
                    else:
                        booleans.append(False)
                booleans = tuple(booleans)
                prob_dict[booleans] = prob
        nodes.append(Node(name, dependents, prob_dict))
    return nodes



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
    # nodes = [
    #     Node("Chair", prob_dict={True: 0.8}),
    #     Node("Sport", prob_dict={True: 0.02}),
    #     Node("Back", dependents=["Chair", "Sport"], prob_dict={
    #         (True, True): 0.9,
    #         (True, False): 0.2,
    #         (False, True): 0.9,
    #         (False, False): 0.01
    #     }),
    #     Node("Ache", dependents=["Back"], prob_dict={(True,): 0.7, (False,): 0.1})
    # ]

    nodes = load_from_json("cw7/nodes_structure.json")
    samples = [generate_sample(nodes) for _ in range(100)]
    for sample in samples:
        print(sample)


