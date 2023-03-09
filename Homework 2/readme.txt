The code is broken up into three sections, A, B, and C, and each section completes a similar task: it reads dates in a particular format, compares them to the current date, and outputs or writes to a file the dates that are on or before the current date.
PART A
To work with dates and times, the code imports the datetime module from Python's standard library.
The user is prompted to enter a date in part A using the format "Month day, year" (for example, "March 8, 2023"), and the code then checks to see if it matches the text "-1" that denotes the end of input. The code prints the date in the format "month/day/year" (for example, "3/8/2023") if the input is a valid date and is on or before the current date.

PART B
In section B, dates are read line by line from a file called inputDates.txt until the string "-1" is encountered. Then, if all of the dates are correct and fall on or before the current date, they are printed using the same format as part A.

PART C
In part C, the code reads dates from inputDates.txt similarly to part B, but instead of outputting the dates, if they are correct and on or before the current date, it writes them to a new file called parsedDates.txt. Similar to section A, the dates are written in the same format.
