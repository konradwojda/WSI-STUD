from math import log
from collections import Counter

class TrainingSet:
    def __init__(self, class_ = None, attributes = None):
        self.attributes = attributes if attributes else []
        self.class_ = class_


class Node:
    def __init__(self, attribute=None, children=None):
        self.attribute = attribute
        self.children = children

    def classify(self, sample):
        if sample[self.attribute] in self.children:
            return self.children[sample[self.attribute]].classify(sample)
        else:
            classes = [child.classify(sample) for child in self.children.values()]
            class_counter = Counter(classes)
            return class_counter.most_common(1)[0][0]


class Leaf:
    def __init__(self, class__=None):
        self.class_ = class__

    def classify(self, sample):
        return self.class_



def divide_by_attr(pairs, attr, value):
    return [elem for elem in pairs if elem.attributes[attr] == value]


def entropy(pairs):
    classes = [pair.class_ for pair in pairs]
    possible_values = list(set(classes))
    return -sum(classes.count(value) * log(classes.count(value)) for value in possible_values)


def divided_entropy(pairs, attr):
    possible_values = list(set([pair.attributes[attr] for pair in pairs]))
    divided = [divide_by_attr(pairs, attr, value) for value in possible_values]
    return sum((len(subset)/len(pairs)) * entropy(subset) for subset in divided)


def inf_gain(pairs, attr):
    return (entropy(pairs) - divided_entropy(pairs, attr))


def id3(pairs, attributes):
    if len({pair.class_ for pair in pairs}) == 1:
        return Leaf(pairs[0].class_)

    if not attributes:
        return Leaf(Counter([pair.class_ for pair in pairs]).most_common(1)[0][0])

    best_attr = max(attributes, key=lambda attr: inf_gain(pairs, attr))

    possible_values = list({pair.attributes[best_attr] for pair in pairs})

    divided = {value: divide_by_attr(pairs, best_attr, value) for value in possible_values}

    new_attributes = attributes.copy()
    new_attributes.discard(best_attr)

    return Node(best_attr,
                {attr: id3(new_pairs, new_attributes) for attr, new_pairs in divided.items()})


if __name__ == "__main__":
    node = id3(
        [
            TrainingSet("0", ["A", "1"]),
            TrainingSet("1", ["B", "1"]),
            TrainingSet("1", ["B", "2"]),
            TrainingSet("0", ["B", "2"]),
            TrainingSet("1", ["B", "3"]),
        ],
        set((0, 1))
    )

