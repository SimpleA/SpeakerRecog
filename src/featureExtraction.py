#!/usr/bin/env python3
"""Funtion for feature extractoin
Chin-Cheng Chan. June 2017
"""
import subprocess as subp
import os
from util import checkFolder

def extractFeat(dataList, featType = "SPro", inFormat = "SPH"):
    dataPath = os.path.dirname(dataList)
    if inFormat != "SPH":
        print("Only SPH format is supported for now")
        assert(inFormat == "SPH")
    if featType == "SPro":
        with open(dataList) as dl:
            for l in dl:
                l = l.rstrip("\n")
                print("Extracting feature for {}".format(l))
                inPath = os.path.join(dataPath, "sph", l+".sph")
                checkFolder(os.path.join(dataPath, "prm"))
                outPath = os.path.join(dataPath, "prm", l+".tmp.prm")
                argu = ["bin/sfbcep", "-m", "-k", "0.97"]
                argu += ["-p19", "-n", "24", "-r", "22", "-e", "-D"]
                argu +=  ["-A", "-F", "SPHERE", inPath, outPath]
                subp.run(argu, check=True)
    elif featType == "HTK":
        print("Only SPro format if supported for now")
        assert(featType == "SPro")
    else:
        print("Invalid input audio format {}".format(inFormat))
        raise(ValueError("Invalid input audio format "))

def procFeature(dataList):
    dataPath = os.path.dirname(dataList)
    print("Normalize energy")
    argu = ["bin/NormFeat", "--config", "cfg/NormFeat_energy_SPro.cfg"]
    argu += ["--inputFeatureFilename", dataList]
    argu += ["--featureFilesPath", os.path.join(dataPath, "prm/")]
    subp.run(argu, check=True)

    print("Energy detector")
    lblPath = os.path.join(dataPath, "lbl/")
    checkFolder(lblPath)
    argu = ["bin/EnergyDetector", "--config", "cfg/EnergyDetector_SPro.cfg"]
    argu += ["--inputFeatureFilename", dataList]
    argu += ["--featureFilesPath", os.path.join(dataPath, "prm/")]
    argu += ["--labelFilesPath", lblPath]
    subp.run(argu, check=True)

    print("Normalize features")
    argu = ["bin/NormFeat", "--config", "cfg/NormFeat_SPro.cfg"]
    argu += ["--inputFeatureFilename", dataList]
    argu += ["--featureFilesPath", os.path.join(dataPath, "prm/")]
    argu += ["--labelFilesPath", lblPath]
    subp.run(argu, check=True)
