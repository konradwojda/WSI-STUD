import csv
from os import read
from id3 import TrainingPair


def read_from_file(path):
    pairs = []
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 1
        for row in csv_reader:
            class_ = row[0]
            attributes = [attr for attr in row[1:]]
            pairs.append(TrainingPair(class_, attributes))
    return pairs



if __name__ == "__main__":
    pairs = read_from_file("cw4/data/breast-cancer.data")