from reader import read_from_file
from id3 import id3
from random import shuffle
from collections import Counter
import numpy as np


# DATA_PATH = "cw4/data/agaricus-lepiota.data"

DATA_PATH = "cw4/data/breast-cancer.data"
data1_positive = 'e'
data1_negative = 'p'

data2_positive = 'recurrence-events'
data2_negative = 'no-recurrence-events'


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
    success_list = []
    mistake_matrix = np.array([[0, 0], [0, 0]])
    for pair in testing_pairs:
        try:
            result = node.classify(pair.attributes)
            expected = pair.class_
            success_list.append(expected == result)
            if (expected == result):
                if expected == data2_positive:
                    mistake_matrix[0][0] += 1
                elif expected == data2_negative:
                    mistake_matrix[1][1] += 1
            else:
                if expected == data2_positive:
                    mistake_matrix[0][1] += 1
                elif expected == data2_negative:
                    mistake_matrix[1][0] += 1
        except KeyError as e:
            success_list.append("***cannot classify***")
            # print(e)
    print(Counter(success_list))
    print(mistake_matrix)
    print("Accuracy:")
    print((mistake_matrix[0][0] + mistake_matrix[1][1])/len(testing_pairs))

if __name__ == "__main__":
    test_id3()
