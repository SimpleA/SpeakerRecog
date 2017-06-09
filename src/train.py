#!/usr/bin/env python3
"""Functions for training UBM and adaptation
Chin-Cheng Chan. June 2017.
"""
import subprocess as subp

def trainUBM():
    argu = ["bin/TrainWorld", "--config", "cfg/TrainWorld.cfg"]
    ret = subp.run(argu, check=True, stdout=subp.PIPE)
    with open("log/TrainWorld.log", "w") as tw:
        tw.write(str(ret.stdout))

def trainAdapt():
    argu = ["bin/TrainTarget", "--config", "cfg/TrainTarget.cfg"]
    ret = subp.run(argu, check=True, stdout=subp.PIPE)
    with open("log/TrainTarget.log", "w") as tw:
        tw.write(str(ret.stdout))
