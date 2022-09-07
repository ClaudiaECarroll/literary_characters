##Instructions for this program: 1. Your working directory muct contain this script and the folder containing the files you want to process. From the command line, make sure parallel is installed. Then enter the following: find ./folder_name/*.txt | parallel python book2entities.py {} 
#The program will produce a folder titles "main_characters" and populate it with subdirectories, each with the same name as one of the files in the original folder. Each of those subdirectories will contain two files--one for entities and one for tokens.

#This program makes use of David Bamman's python BookNLP (https://github.com/booknlp/booknlp). All credit to him on that.

# configure
PARAMETERS = { "pipeline":"entity", "model":"big" }
LANGUAGE   = 'en'

# require
from imp import source_from_cache
from booknlp.booknlp import BookNLP
import sys
import os
import pathlib
import shutil

# sanity check

# get input
file = sys.argv[1]
directory = pathlib.Path(file).stem
id = pathlib.Path(file).stem

parent_dir = os.getcwd()

if not os.path.isdir("main_characters"):
    new_folder = "main_characters"
    path_2 = os.path.join(parent_dir, new_folder)
    os.mkdir(path_2)

# initialize
booknlp = BookNLP( LANGUAGE, PARAMETERS )

# do the work and done
booknlp.process( file, directory, id )

path = os.path.join(parent_dir, directory)

shutil.move(path, "main_characters")

exit()

