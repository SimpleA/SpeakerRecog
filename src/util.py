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

def checkFolder(fold):
    if os.path.exists(fold):
        return True
    else:
        print("Directory {} not detected. Automatically create it".format(fold))
        os.mkdir(fold)
        return False
