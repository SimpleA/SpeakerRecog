#!/usr/bin/env python3
""" Helper function for splitting training and testing data
DEPENDENCIES: This function requires the tool `sox`
Chin-Cheng Chan. June 2017.
"""
import sys
import os
import subprocess as subp

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("[Usage]: python convertAudio.py [path_to_data_folder]")
    foldName = sys.argv[1]
    listFile = os.path.join(foldName, "datalist.lst")

    dataFiles = []
    with open(listFile) as lf:
        dataFiles = [l.rstrip("\n") for l in lf]

    for auf in dataFiles:
        base = auf.split(".")[0]
        sphFile = os.path.join(foldName, "sph", base+".sph")
        print("Processing file {}".format(base + ".sph"))
        # get audio length
        soxRet = subp.run(["soxi", "-D", sphFile], check=True, stdout=subp.PIPE)
        audLen = float(soxRet.stdout)
        print("Detected audio length {} seconds".format(audLen))
        # trim audio
        print("trimming audio {}".format(sphFile))
        trainFile = os.path.join(foldName, "sph", base+"_train.sph")
        testFile = os.path.join(foldName, "sph", base+"_test.sph")
        soxRet = subp.run(["sox", sphFile, trainFile, "trim",\
                            "00:10", str(audLen - 10)], check=True)
        soxRet = subp.run(["sox", sphFile, testFile, "trim",\
                            "0", "00:10"], check=True)
        print("Trimed audio saved to {} and {}".format(trainFile, testFile))
