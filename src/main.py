#!/usr/bin/env python3
"""main function for the project
"""
from featureExtraction import extractFeat, procFeature
from util import syncDataList, genTrainModelNdx, genComputeTestNdx
from train import trainAdapt
from test import computeTest

if __name__ == "__main__":
    syncDataList("data/data_train")
    syncDataList("data/data_test")
    print("Performing feature extraction")
    extractFeat("data/data_train/data.lst")
    extractFeat("data/data_test/data.lst")

    print("Processing features")
    procFeature("data/data_train/data.lst")
    procFeature("data/data_test/data.lst")

    genTrainModelNdx("data/data_train")
    genComputeTestNdx("data/data_train")
    trainAdapt()
    computeTest()
