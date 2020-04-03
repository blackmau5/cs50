import sys, csv

#Define the argument passing and usage
if len(sys.argv) != 3:
    print('Usage: python dna.py data.csv sequence.txt')
    sys.exit()

#Open the csv file
with open(sys.argv[1], newline='') as f:
    csv_reader = list(csv.reader(f))
    STR_list = []
    db_list = []
    for i in range(1, len(csv_reader[0])):
        STR_list.append(csv_reader[0][i])
    for i in csv_reader:
        db_list.append(i)

#Open the txt file
with open(sys.argv[2]) as f2:
    str_txt = str(f2.read().strip())

#Calculating maximum consecutive matches of STRs or returning False if no matches found
def match(STR_list):
    count = 1
    max_count = 0
    match_list = []
    for i in STR_list:
        if str_txt.find(i) != -1:
            j = str_txt.find(i)
            while j < len(str_txt)-len(i)+1:
                if str_txt[j-len(i):j] == str_txt[j:j+len(i)] == i:
                    count += 1
                    j += len(i)
                elif count > max_count:
                    max_count = count
                    count = 1
                else:
                    j += 1
            match_list.append(str(max_count))
            max_count = 0
            count = 1
        else:
            return False
    return match_list

match_list = match(STR_list)

#Compare the list of found matches with the list from the opened csv
def compare_matches():
    for i in range(1, len(db_list)):
        db_lists = []
        for j in range(1, len(db_list[1])):
            db_lists.append(db_list[i][j])
        if match_list == db_lists:
            return db_list[i][0]
    return 'No match'

#Print the name of the matching person's STR or 'No match' if no match found
if match_list is False:
    print('No match')
else:
    print(compare_matches())
