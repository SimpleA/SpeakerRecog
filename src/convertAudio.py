#!/usr/bin/env python3
""" Helper fnction for converting audio to the sphere format
DEPENDENCIES: This function requires the tool `sox`
Chin-Cheng Chan. June 2017.
"""
import sys
import os
import subprocess as subp

def checkFolder(fold):
    if os.path.exists(fold):
        return True
    else:
        print("Directory {} not detected. Automatically create it".format(fold))
        os.mkdir(fold)
        return False

if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print("[Usage]: python convertAudio.py [path_to_data_folder]")
    foldName = sys.argv[1]
    listFile = os.path.join(foldName, "datalist.txt")

    dataFiles = []
    with open(listFile) as lf:
        dataFiles = [l.rstrip("\n") for l in lf]
    for auf in dataFiles:
        auFile = os.path.join(foldName, "input", auf)
        # detect audio file format
        inFormat = auf.split(".")[1]
        print("Detected input format = {}".format(inFormat))

        # fetch audio meta-data
        soxRet = subp.run(["soxi", "-r", str(auFile)], check=True, stdout=subp.PIPE)
        sampRate = int(soxRet.stdout)
        print("Detected sampling rate = {}".format(sampRate))

        # convert file
        ouf = auf.split(".")[0] + ".sph"
        checkFolder(os.path.join(foldName, "sph"))
        outFile = os.path.join(foldName, "sph", ouf)
        print("Convertin to sphere format...")
        soxRet = subp.run(["sox", "-t", inFormat, auFile, "-r", str(sampRate),
                        "-t", "sph", outFile], check=True)
        print("Conversion succeed. File saved to {}".format(outFile))
