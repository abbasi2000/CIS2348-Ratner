# EMAD ABBASI
# 2095022
# Get input from the user
input_str = input()

# Convert the input string to a list of integers
input_list = list(map(int, input_str.split()))

# Filter out the non-negative integers and sort them in ascending order
non_negative_integers = sorted([num for num in input_list if num >= 0])

# Print the sorted non-negative integers separated by spaces
output_str = ' '.join(map(str, non_negative_integers))
print(output_str, end=' ')