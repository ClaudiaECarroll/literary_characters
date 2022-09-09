#!/usr/bin/env python
# coding: utf-8

#Instructions: Given a megafolder containing many subfolders, which in turn contain the .entities outputs of bookNLP, get the most mentioned proper name and print it to a new file .chr with same name as novel file to the megafolder. This program should be in the same working directory as the mega folder.


import pandas as pd
import sys
import pathlib
import os
import shutil

main_folder = sys.argv[1]


for x in os.listdir(main_folder):
    xname = os.path.join(main_folder, x)  
    for f in os.listdir(xname):
        filename = os.path.join(xname, f)
        if filename.endswith(".entities"):
            print(filename)
            n = 1
            char_file  = (os.path.basename(filename).split(".")[0] + ".chr")
            char = open(char_file, "w")
            df = pd.read_csv(filename, sep="\t")
            df_characters = df.loc[(df["prop"] == "PROP") & (df["cat"] == "PER")]
            main_character = df_characters["text"].value_counts().index.tolist()[:n]        
            print(main_character[0], file=char)
            shutil.move(char_file, main_folder)
         








