#!/usr/bin/env python3
"""Functions for speaker identification
Chin-Cheng Chan. June 2017.
"""
import subprocess as subp

def computeTest():
    argu = ["bin/ComputeTest", "--config", "cfg/ComputeTest_GMM.cfg"]
    ret = subp.run(argu, check=True, stdout=subp.PIPE)
    with open("log/ComputeTest_GMM.log", "w") as tw:
        tw.write(str(ret.stdout))
