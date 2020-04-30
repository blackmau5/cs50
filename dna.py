#Problem description can be found here: https://cs50.harvard.edu/x/2020/psets/6/dna/
import csv
import sys

# Define the argument passing and usage
if len(sys.argv) != 3:
    print('Usage: python dna.py data.csv sequence.txt')
    sys.exit()

# Open the csv file and create 2 lists: one with all csv lines as lists and another one with STRs
with open(sys.argv[1], newline='') as csv_file:
    db_list = list(csv.reader(csv_file))
    str_list = db_list[0][1:]

with open(sys.argv[2]) as txt_file:
    str_txt = str(txt_file.read().strip())


# Calculate maximum consecutive matches of STRs or returning False if no matches found
def match():
    match_list = []
    for i in str_list:
        if i in str_txt:
            count = 1
            max_count = 0
            j = str_txt.find(i) + len(i)
            while j < len(str_txt) - len(i) + 1:
                if str_txt[j - len(i):j] == str_txt[j:j + len(i)] == i:
                    count += 1
                    j += len(i)
                elif count > max_count:
                    max_count = count
                    count = 1
                else:
                    j += 1
            # This if block catches the maximum occurrence if the longest sequence is located at the end of the str_txt
            if count > max_count:
                max_count = count
            match_list.append(str(max_count))
        else:
            return False
    return match_list


# Compare the list of found matches with the lists from the csv file
def compare_matches():
    for repeats_list in db_list[1:]:
        sequence_list = [repeats for repeats in repeats_list[1:]]
        if match() == sequence_list:
            return repeats_list[0]
    return 'No match'


# Print the name of the matching person's STR or 'No match' if no match found
if match():
    print(compare_matches())
else:
    print('No match')
