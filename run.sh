#!usr/bin/env bash

# next I'll make sure that all my programs (written in Python in this example) have the proper permissions
chmod a+x ./src/my_word_count.py
chmod a+x ./src/my_running_median.py

# finally I'll execute my programs, with the input directory wc_input and output the files in the directory wc_output
python3 ./src/my_word_count.py ./wc_input ./wc_output/wc_result.txt
python3 ./src/my_running_median.py ./wc_input ./wc_output/med_result.txt
