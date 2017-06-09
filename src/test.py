#!/usr/bin/env python3
"""Functions for speaker identification
Chin-Cheng Chan. June 2017.
"""
import subprocess as subp

def computeTest():
    argu = ["bin/ComputeTest", "--config", "cfg/ComputeTest_GMM.cfg"]
