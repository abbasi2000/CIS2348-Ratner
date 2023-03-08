# 2095022 # EMAD ABBASI
# WORD FREQUENCIES (LISTS)

import csv  # it is a built in module
file_name = input()
with open(file_name, 'r') as input_file:  # will read file then iterate over values
    reader = csv.reader(input_file)
# creating dictionaries
    word_frequencies = {}
# iterating code
    for row in reader:  # goes over rows
        for word in row: # goes over words
            word = word.lower().strip()  # lower cases and gets rid of unnecessary spaces

            if word not in word_frequencies:
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

    for word, frequencies in word_frequencies.items():
        print(word, frequencies)

