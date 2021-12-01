from math import log
from collections import Counter

class TrainingPair:
    """
    attributes - lista atrybutów
    class_ - finalna decyzja wynikająca z atrybutów
    """
    def __init__(self, class_ = None, attributes = None):
        self.attributes = attributes if attributes else []
        self.class_ = class_


class Node:
    """
    attribute - number atrybutu, który opisuje węzeł
    children - dict, który dla każdego z atrybutów ma przypisany węzeł
    """
    def __init__(self, attribute=None, children=None):
        self.attribute = attribute
        self.children = children

    def classify(self, sample):
        return self.children[sample[self.attribute]].classify(sample)

    def to_dot(self) -> str:
        self_name = f"node_{id(self)}"

        # Create a node for the current node
        x = f'  {self_name} [label="Split on attr {self.attribute}"];\n'

        # Create all the edges
        for edge_label, child in self.children.items():
            # Add dot from the child (to get its definition before inserting the edge)
            x += child.to_dot()

            # Add the edge to the child
            child_name = f"node_{id(child)}"
            escaped_edge_label = edge_label.encode("unicode_escape") \
                                           .decode("ascii") \
                                           .replace('"', r'\"')
            x += f'  {self_name} -> {child_name} [label="{escaped_edge_label}"];\n'

        return x



class Leaf:
    """
    class_ - finalna decyzja
    """
    def __init__(self, class__=None):
        self.class_ = class__

    def classify(self, sample):
        return self.class_


    def to_dot(self) -> str:
        class_escaped = self.class_.encode("unicode_escape") \
                                   .decode("ascii") \
                                   .replace('"', r'\"')
        return f'  node_{id(self)} [shape=box, label="{class_escaped}"];\n'



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
            TrainingPair("0", ["unused", "A", "1"]),
            TrainingPair("1", ["unused", "B", "1"]),
            TrainingPair("1", ["unused", "B", "2"]),
            TrainingPair("0", ["unused", "B", "2"]),
            TrainingPair("1", ["unused", "B", "3"]),
        ],
        set((1, 2))
    )

    print("digraph {")
    print(node.to_dot())
    print("}")

