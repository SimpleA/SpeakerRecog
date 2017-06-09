"""Utilities for the project
"""
import os

# Automatically generate data.lst from .sph files
def syncDataList(dataPath):
    sphPath = os.path.join(dataPath, "sph")
    files = os.listdir(sphPath)
    with open(os.path.join(dataPath, "data.lst"), "w") as outFile:
        fi = [l.rstrip("\n").split(".")[0] for l in files \
            if len(l) > 5 and l[-3:] == "sph" and l[0] != "."]
        fi = sorted(fi)
        outFile.write("\n".join(fi))

# generate the ndx file
def genTrainModelNdx(dataPath):
    with open(os.path.join(dataPath, "data.lst")) as dl:
        data = [l.rstrip("\n") for l in dl]
    cnt = 0
    with open("ndx/trainModel.ndx", "w") as tm:
        for d in data:
            cntStr = "0" * (2 - len(str(cnt))) + str(cnt)
            tm.write("spk"+cntStr + " " + d + "\n")
            cnt += 1

def genComputeTestNdx(dataPath):
    first = []
    second = []
    with open("ndx/trainModel.ndx") as tm:
        for l in tm:
            fie = l.rstrip("\n").split(" ")
            first.append(fie[0])
            second.append(fie[1])
    with open("ndx/computetest_gmm_target-seg.ndx", "w") as nd:
        for s in second:
            cont = [s] + first
            nd.write(" ".join(cont) + "\n")

def checkFolder(fold):
    if os.path.exists(fold):
        return True
    else:
        print("Directory {} not detected. Automatically create it".format(fold))
        os.mkdir(fold)
        return False
