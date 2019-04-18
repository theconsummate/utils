import sys
import random

"""
python3 make_tts_dataset.py <path to file>
path to file has to be absolute path
"""
fname = sys.argv[1]
dirname = fname.replace("txt.done.data", "") + "wav/"

def process_dataset(arr, outfile):
    fo = open(outfile, 'w')
    for line in arr[:5]:
        """
        an example of a single line.
        line = '( arctic_a0001 "Author of the danger trail, Philip Steels, etc." )\n'
        """
        wav, text = line.strip()[2:-2].replace('"', "").split(" ", 1)
        fo.write(dirname+wav+".wav|" + text+"\n")
    fo.close()

f = open(fname, 'r')
contents = random.shuffle(f.readlines())
f.close()

size = len(contents)

# train
process_dataset(contents[:int(size*0.95)], "train.txt")

# dev
process_dataset(contents[int(size*0.95): int(size*0.97) ], "dev.txt")

# test
process_dataset(contents[int(size*0.97):], "test.txt")