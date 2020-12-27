import csv

def process_line(line):
    remainder, password = line.split(": ")
    remainder, letter = remainder.split(" ")
    min_required, max_required = remainder.split("-")
    return (int(min_required), int(max_required), letter, password)

entries = []
with open('input.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    entries = [process_line(row[0]) for row in csv_reader]

def password_policy_1(entries):
    valid_passwords = 0
    for min_required, max_required, letter, password in entries:
        count = password.count(letter)
        if min_required <= count <= max_required:
            valid_passwords = valid_passwords+1
    return valid_passwords

def password_policy_2(entries):
    valid_passwords = 0
    for index_1, index_2, letter, password in entries:
        match_1 = password[index_1-1] == letter
        match_2 = password[index_2-1] == letter

        if (not match_1 == match_2) and (match_1 or match_2):
            valid_passwords = valid_passwords+1
    return valid_passwords 

print(password_policy_1(entries))
print(password_policy_2(entries))