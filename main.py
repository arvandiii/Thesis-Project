import os
from clean import clean
from filter_lang import filter_lang
from filter_relevant import filter_relevant

stages = [clean, filter_lang, filter_relevant]

def run(dir_in, dir_out):
    current_dir_in = dir_in
    for stage in stages:
        dir_out_sub = os.path.join(dir_out, stage)
        stage(current_dir_in, dir_out_sub)
        current_dir_in = dir_out_sub

if __name__ == 'main':
    dir_in = input("Enter the output directory: ")
    dir_out = input("Enter the output directory: ")
    run(dir_in, dir_out)