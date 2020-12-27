import csv

entries = []
with open('input.csv') as file:
    entries = [int(row) for row in file.readlines()]

TARGET = 2020
def solve_2(entries):
    for index_a, num_a in enumerate(entries):
        for index_b, num_b in enumerate(entries):
            if ((num_a + num_b) == TARGET) and index_a != index_b:
                return num_a*num_b

def solve_3(entries):
    for index_a, num_a in enumerate(entries):
        for index_b, num_b in enumerate(entries):
            for index_c, num_c in enumerate(entries):
                if ((num_a + num_b + num_c) == TARGET) and (index_a != index_b != index_c):
                    return num_a*num_b*num_c

print(solve_2(entries))
print(solve_3(entries))


