# 2095022 # EMAD ABBASI
# DATE READER/MODIFIER
# TRYING TO UNDERSTAND COMMIT CHANGES, i'll write the full code here then figure that out later
# initial commit change done, visible in history but still unsure on how to add a change
from datetime import datetime

with open('inputDates.txt') as f:
    for line in f:
        date_str = line.strip()
        if date_str == "-1":
            break
