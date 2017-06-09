#!/usr/bin/env python3
import sys

if __name__ == "__main__":
    if (len(sys.argv) != 3):
        print("[Usage]: python computeAccu.py [path_to_res] [path_to_ans]")
        print("Setting to default: resfile=res/target-seg_gmm.res,"
            " ansfile=ndx/trainModel.ndx")
        resPath = "res/target-seg_gmm.res"
        ansPath = "ndx/trainModel.ndx"
    else:
        resPath = sys.argv[1]
        ansPath = sys.argv[2]
    # parse res file
    spk = dict()
    with open(resPath) as res:
        for l in res:
            fie = l.rstrip("\n").split(" ")
            spkName = fie[1]
            if spkName not in spk:
                spk[spkName] = [fie[3], float(fie[4])]
            elif spk[spkName][1] < float(fie[4]):
                spk[spkName] = [fie[3], float(fie[4])]
    # parse ans
    ans = dict()
    with open(ansPath) as af:
        for l in af:
            fie = l.rstrip("\n").split(" ")
            ans[fie[0]] = fie[1]
    # compute accuracy
    cor = 0 # correct detection
    for key, val in spk.items():
        if val[0] == ans[key]:
            cor += 1
    print("Accuracy = {}".format(float(cor) / len(spk)))
