#Part A - Reading dates from input and outputting correct dates:
from datetime import datetime

current_date = datetime.now().date()

while True:
date_str = input()
if date_str == '-1':
break
date = datetime.strptime(date_str, '%B %d, %Y').date() if date_str.count(',') == 1 else None
if date and date <= current_date:
print(date.strftime('%-m/%-d/%Y'))

#Part B - Reading dates from input file and outputting correct dates:
from datetime import datetime

current_date = datetime.now().date()

with open('inputDates.txt') as f:
for line in f:
line = line.strip()
if line == '-1':
break
date = datetime.strptime(line, '%B %d, %Y').date() if line.count(',') == 1 else None
if date and date <= current_date:
print(date.strftime('%-m/%-d/%Y'))

#Part C - Reading dates from input file and writing correct dates to output file:
from datetime import datetime

current_date = datetime.now().date()

with open('inputDates.txt') as f, open('parsedDates.txt', 'w') as out_file:
for line in f:
line = line.strip()
if line == '-1':
break
date = datetime.strptime(line, '%B %d, %Y').date() if line.count(',') == 1 else None
if date and date <= current_date:
out_file.write(date.strftime('%-m/%-d/%Y') + '\n')
from datetime import datetime

current_date = datetime.now().date()

while True:
    date_str = input()
    if date_str == '-1':
        break
    try:
        date = datetime.strptime(date_str, '%B %d, %Y').date()
        if date <= current_date:
            print(date.strftime('%-m/%-d/%Y'))
    except ValueError:
        continue

#Part B - Reading dates from input file and outputting correct dates:

from datetime import datetime

current_date = datetime.now().date()

with open('inputDates.txt') as f:
    for line in f:
        line = line.strip()
        if line == '-1':
            break
        try:
            date = datetime.strptime(line, '%B %d, %Y').date()
            if date <= current_date:
                print(date.strftime('%-m/%-d/%Y'))
        except ValueError:
            continue

#Part C - Reading dates from input file and writing correct dates to output file:

from datetime import datetime

current_date = datetime.now().date()

with open('inputDates.txt') as f, open('parsedDates.txt', 'w') as out_file:
    for line in f:
        line = line.strip()
        if line == '-1':
            break
        try:
            date = datetime.strptime(line, '%B %d, %Y').date()
            if date <= current_date:
                out_file.write(date.strftime('%-m/%-d/%Y') + '\n')
        except ValueError:
            continue