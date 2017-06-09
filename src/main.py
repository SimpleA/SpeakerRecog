#!/usr/bin/env python3
"""main function for the project
"""
from featureExtraction import extractFeat, procFeature
from util import syncDataList
from train import trainAdapt
from test import computeTest

if __name__ == "__main__":
    # syncDataList("data/user_train")
    # syncDataList("data/user_test")
    # print("Performing feature extraction")
    # extractFeat("data/user_train/data.lst")
    # extractFeat("data/user_test/data.lst")
    #
    # print("Processing features")
    # procFeature("data/user_train/data.lst")
    # procFeature("data/user_test/data.lst")
    # trainAdapt()
    computeTest()
