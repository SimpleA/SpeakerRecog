#!/usr/bin/env python3
"""main function for the project
"""
from featureExtraction import extractFeat, procFeature

if __name__ == "__main__":
    print("Performing feature extraction")
    extractFeat("data/memo/datalist_train.lst")
    extractFeat("data/memo/datalist_test.lst")

    print("Processing features")
    procFeature("data/memo/datalist_train.lst")
    procFeature("data/memo/datalist_test.lst")
