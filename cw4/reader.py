import csv
from os import read
from id3 import TrainingSet


def read_from_file(path):
    pairs = []
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            class_ = row[0]
            attributes = [attr for attr in row[1:]]
            pairs.append(TrainingSet(class_, attributes))
    return pairs



if __name__ == "__main__":
    pairs = read_from_file("cw4/data/breast-cancer.data")