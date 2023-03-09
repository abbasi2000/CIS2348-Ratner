# 2095022 # EMAD ABBASI
# DATE READER/MODIFIER
# TRYING TO UNDERSTAND COMMIT CHANGES, i'll write the full code here then figure that out later
# initial commit change done, visible in history but still unsure on how to add a change
from datetime import datetime

# PartA Write a program that reads dates from input, one date per line. Each
# date's format must be as follows: March 1, 1990. Ignore any dates
# that are later than the current date. Output each correct date as:
# 3/1/1990.

while True:
    date_str = input()
    if date_str == '-1':
        break
    try:
        date_correct = datetime.strptime(date_str, '%B %d, %Y')
        current_date = datetime.now()
        if date_correct <= current_date:
            print(date_correct.strftime('%-m/%-d/%Y'))
    except ValueError:
        pass

        try:
            date = datetime.strptime(date_str, '%B %d, %Y')
            if date <= datetime.now():
                print(date.strftime('%-m/%-d/%Y'))
        except ValueError:
            pass

    # Part B After the program is working as above, modify the program so that it
    # reads all dates from an input file “inputDates.txt” (an Example file is
    # attached).

    with open('inputDates.txt', 'r') as input_file:
        input_lines = input_file.readlines()

    for date_str in input_lines:
        try:
            date_obj = datetime.strptime(date_str.strip(), '%B %d, %Y')
            current_date = datetime.now()
            if date_obj <= current_date:
                print(date_obj.strftime('%-m/%-d/%Y'))
        except ValueError:
            pass

    # Part C Modify your program further so that after parsing all dates from the
    # input file “inputDates.txt”, it writes out the correct ones into an
    # output file called: “parsedDates.txt”.

    with open('inputDates.txt', 'r') as input_file, open('parsedDates.txt', 'w') as output_file:
        input_lines = input_file.readlines()

        for date_string in input_lines:
            try:
                date_obj = datetime.strptime(date_string.strip(), '%B %d, %Y')
                current_date = datetime.now()
                if date_obj <= current_date:
                    output_file.write(date_obj.strftime('%-m/%-d/%Y') + '\n')
            except ValueError:
                pass