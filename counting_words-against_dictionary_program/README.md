This folder contains two programs. One to count the words in a plain text file against a dictionary of words, and one to do the same by oterating through multiple files in a directory and returning the number of relevant words in each file. The programs are designed to be used with a dictionary and text contained in plain text files.

**Instructions:**
To use the first program (single file), first navigate to the directory containing both the dictionary file and the text file you wish to count against. Download the python script into the same directory, and run it with the text file name as the first argument, and the dictionary file name as the second argument. 
Example:
$ python3 word_count_from_dictionary.py textfile.txt dictionary.txt
The output should be an integer.

To use the second program, iterating through files in a directory and returning an integer value for each, you will need to specify the directory address of the folder containing the files you want to iterate through. Follow the instructions, for the first program, but with the directory address for the desired folder in place of the text file name as the first argument.
Example:
$ python3 word_count_from_dictionary_iterating.py ~/Documents/programming/foldername dictionary.txt
The output should be a list of integers.

**Notes:**
1. The second program (for iterating through files), is written to only iterate through the .txt files in the folder.
2. The programs both use nltk for tokenizing. When you run the program, the NLTK downloader will open. Download the packages, and then press File, Exit. The program will not continue until you do so.

