#!/usr/bin/env python3
"""Functions for training UBM and adaptation
Chin-Cheng Chan. June 2017.
"""
import subprocess as subp

def trainUBM():
    argu = ["bin/TrainWorld", "--config", "cfg/TrainWorld.cfg"]
    ret = argu.run(argu, check=True, stdout=subp.PIPE)
    with open("log/TrainWorld.log") as tw:
        tw.write(ret)

def trainAdapt():
    argu = ["bin/TrainTarget", "--config", "cfg/TrainTarget.cfg"]
    ret = argu.run(argu, check=True, stdout=subp.PIPE)
    with open("log/TrainTarget.log") as tw:
        tw.write(ret)
