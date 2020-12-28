
mymap = []
with open('input', 'r') as file:
    mymap = [row.strip() for row in file.readlines()]

TREE = '#'
SNOW = '.'

def count_trees(mymap, slope = [3, 1]):
    slope_x, slope_y = slope
    num_trees = 0
    position_x = 0
    position_y = 0

    for position_y in range(0, len(mymap), slope_y):
        row = mymap[position_y]

        if position_x >= len(row):
            position_x = position_x - len(row)
        
        cell = row[position_x]

        if cell == TREE:
            num_trees = num_trees + 1

        position_x = position_x + slope_x
    
    return num_trees


def check_all_slopes(mymap):
    slopes = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2]
    ]
    slopes_trees = [count_trees(mymap, slope = slope) for slope in slopes]

    result = 1
    for num_trees in slopes_trees:
        result = result * num_trees
    return result


print(check_all_slopes(mymap))