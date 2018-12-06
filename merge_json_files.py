import sys
import json
# usage python merge_json_files.py fullpath1 fullpath2 fulloutputpath

f1 = open(sys.argv[1])
f2 = open(sys.argv[2])

j1 = json.load(f1)
j2 = json.load(f2)

out_utts = {}

for key in j1.keys():
    out_utts[key+"_1"] = j1[key]

for key in j2.keys():
    out_utts[key+"_2"] = j1[key]


f3 = open(sys.argv[3], 'w')
json.dum({"utts":out_utts}, f3)