from os import read
from reader import read_from_file
from id3 import *
from random import shuffle


DATA_PATH = "cw4/data/breast-cancer.data"


def test_id3():
    data = read_from_file(DATA_PATH)
    shuffle(data)
    ratio = int(0.6 * len(data))
    training_pairs = data[:ratio]
    testing_pairs = data[ratio:]
    attrs = {x for x in range(len(training_pairs[0].attributes))}
    node = id3(training_pairs, attrs)
    # print("digraph {")
    # print(node.to_dot())
    # print("}")
    for pair in training_pairs:
        try:
            result = node.classify(pair.attributes)
            # print(result)
            # print(pair.class_)
            print(pair.class_ == result)
        except KeyError:
            print("*****cannot classify*****")


if __name__ == "__main__":
    test_id3()