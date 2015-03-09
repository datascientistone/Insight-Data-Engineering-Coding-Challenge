import string
import glob  # used for reading files from specific path
import sys   # used to read command arg 
#input="./wc_input/*"
#output="./wc_result.txt"
#input="F:/coding challenge/wc_input/*"
#output="F:/coding challenge/wc_output/wc_result.txt"
# get the input directory wc_input that contain text files
input=str(sys.argv[1]+"/*")
# get the output file path wc_result
output=str(sys.argv[2])
# get the file paths from the input directory
files=glob.glob(input)
# define a dictionary to store the word and the number of occurences 
wordcount = {}
# parse all the files in the directory
for file in files:
    # open each file for read only access
    with open(file, 'r') as f:
        # for each line in the txt file
        for line in f:
            #get the special characters that should be removed
            special_character_map = dict.fromkeys(map(ord, string.punctuation))
            #remove the special characters from each line 
            line=line.translate(special_character_map)
            # convert all the letters to a lower case and retrieve the words per line 
            words = line.lower().split()
            # for each word check if already occured or not and count the no. of occurences
            for word in words:
                if(word in wordcount): # case of more than one time of occurences 
                    wordcount[word]+=1
                else: # case of first time word appearance
                    wordcount[word]=1
        # open the wc_result text file in write access mode
        with open (output, 'w') as fout:
            # write  the words and number of occurences to the output file 
            for word in sorted(wordcount):
               fout.write(word +"\t" +str(wordcount[word])+ "\n")

