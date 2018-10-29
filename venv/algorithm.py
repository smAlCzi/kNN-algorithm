import numpy as np
import pandas as pd
import math as math
from scipy import spatial
from random import randint

# Load learning and testing data with pandas
data = pd.read_csv('iris.data.learning', header=None)
learn_array = data.values
data = pd.read_csv('iris.data.test', header=None)
test_array = data.values

# Clean array from labels (all left array items are points coordinates)
def removeLabels(array):
    clean_array = []
    for i in array:
        clean_array.append((i[:4]))
    return clean_array

# K-nearest-neighbours class with algorithm
class KNN:
    # Class initialization
    def __init__(self, k, data):
        self.k = k
        self.data = data

    # Calculate distances between points
    def calcDistance(self, i, sample):
        # return spatial.distance.pdist([self.data[i][:4][0], sample])
        return randint(0, 5)

    def predict(self, list):
        for i in range(0, list.shape[0]):
            distances = []
            for j in range(0, self.data.shape[0]):
                print("odleglosc: " + str(self.calcDistance(j, list[i])))
                distances.append(self.calcDistance(j, list[i]))
            print("\n")
        return list

    def score(self, array, labels):
        score = 0
        return score

x = KNN(2, learn_array)

print(x.predict(test_array))