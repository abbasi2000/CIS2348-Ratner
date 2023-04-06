# 2095022
# EMAD ABBASI
input_str = input()

# Convert input string to a list of words
input_list = input_str.split()

# Initialize empty dictionary to store word frequencies
word_frequencies = {}
# Iterate through the input list and update the word frequencies
for word in input_list:
    if word not in word_frequencies:
        word_frequencies[word] = 0
    word_frequencies[word] += 1

# Print the words and their final frequencies
for word in input_list:
    print(f"{word} {word_frequencies[word]}")