import sys
import os
from normalize import normalize
from clean import clean
from filter_lang import filter_lang
from filter_relevant import filter_relevant
from filter_keyword import filter_keyword

stages = [(normalize, True), (clean, True), (filter_keyword, False), (filter_lang, False), (filter_relevant, False)]

def run(dir_in, dir_out):
    current_dir_in = dir_in
    for stage, enabled in stages:
        if not enabled: continue
        dir_out_sub = os.path.join(dir_out, stage.__name__)
        if not os.path.exists(dir_out_sub):
            os.makedirs(dir_out_sub)
        stage(current_dir_in, dir_out_sub)
        current_dir_in = dir_out_sub

if __name__ == '__main__':
    if len(sys.argv) < 3: raise Exception("usage: python3 pre_process dir_in dir_out")
    dir_in = sys.argv[1]
    dir_out = sys.argv[2]
    run(dir_in, dir_out)