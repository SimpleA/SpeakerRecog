"""Utilities for the project
"""
import os

def checkFolder(fold):
    if os.path.exists(fold):
        return True
    else:
        print("Directory {} not detected. Automatically create it".format(fold))
        os.mkdir(fold)
        return False
