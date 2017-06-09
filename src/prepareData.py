#!/usr/bin/env python3
"""Program for preparing training and testing data
DEPENDENCIES: This function requires the tool `sox`
Chin-Cheng Chan. June 2017.
"""
import sys
import os
import re
import subprocess as subp

def checkFolder(fold):
    if os.path.exists(fold):
        return True
    else:
        print("Directory {} not detected. Automatically create it".format(fold))
        os.mkdir(fold)
        return False

def parseSpkFile(filePath):
    idTable = dict()
    rule = re.compile(r"([\d]+)[ ]*\| ([MF]) \| [\w\d-]+[ ]*\| [\d.]+[ ]*\| [\w .]+")

    with open(filePath) as fp:
        for l in fp:
            fie = re.match(rule, l)
            if fie:
                idTable[int(fie.group(1))] = fie.group(2)
    return idTable

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("[Usage]: python3 prepareData.py [path_of_LibriSpeech] [output_path]")
        # raise(Exception("Invalid argument number"))
    trainLen = 60 # length of traning data
    testLen = 10 # length of testing data
    # parse speaker info file
    idTable = parseSpkFile(os.path.join(sys.argv[1], "SPEAKERS.TXT"))
    devPath = os.path.join(sys.argv[1], "test-other")
    outTrainPath = os.path.join(sys.argv[2], "data_train")
    outTestPath = os.path.join(sys.argv[2], "data_test")
    checkFolder(outTrainPath)
    checkFolder(outTestPath)

    folds = os.listdir(devPath)
    for fd in folds:
        base = fd.split(".")[0]
        # skip femail speakers
        if fd[0] == "." or idTable[int(base)] == "F":
            continue
        subfolds = os.listdir(os.path.join(devPath, fd))
        subfolds = sorted(subfolds)

        if subfolds[0][0] == ".":
            audPath = os.path.join(os.path.join(devPath, fd), subfolds[1])
        else:
            audPath = os.path.join(os.path.join(devPath, fd), subfolds[0])
        audFile = os.listdir(audPath)
        audFile = [a for a in audFile if len(a) > 3 and a[-3:] != "txt"]
        print(audFile)

        trn = 0
        tst = 0
        idx = 0
        trainData = []
        testData = []
        # get traning data
        while trn < trainLen:
            soxRet = subp.check_output(["soxi", "-D", os.path.join(audPath, audFile[idx])])
            audLen = float(soxRet)
            trainData.append(os.path.join(audPath, audFile[idx]))
            trn += audLen
            idx += 1
        # get testing data
        while tst < testLen:
            soxRet = subp.check_output(["soxi", "-D", os.path.join(audPath, audFile[idx])],)
            audLen = float(soxRet)
            testData.append(os.path.join(audPath, audFile[idx]))
            tst += audLen
            idx += 1

        # generateing training data
        cmdBase = ["sox"]
        cmdTrain = cmdBase + trainData + [os.path.join(outTrainPath, base+".sph")]
        print(cmdTrain)
        subp.check_output(cmdTrain)
        if len(testData) > 2:
            cmdTest = cmdBase + testData + [os.path.join(outTestPath, base+".sph")]
            subp.check_output(cmdTest)
        else:
            tmp = os.path.join(outTestPath, base+".sph")
            subp.check_output(["sox", "-t", "flac", testData[0], "-t", "sph", tmp])
        # print(cmdTest)
