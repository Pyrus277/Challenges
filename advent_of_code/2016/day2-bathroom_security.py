# Advent of Code 2016: Day 2

# Code works! A lot of repetition tho. See if you can condense by way of functions. 

# Bring in the data
directions = []
with open('day2.txt') as fhand:
    document = fhand.read().splitlines() 
    for line in document:
        directions.append(line)

# directions = ['ULL', 'RRDDD', 'LURDL', 'UUUD']

def part1(directions):
    # setup the bathroom lock
    keypad = [[1,2,3],[4,5,6],[7,8,9]]

    # starting key is 5, set up our code list: 
    row, col, code = 1, 1, [] 

    # move and record
    for line in directions:
        
        # move; go thru all the directions for the line
        for direction in line:
            if direction == "L":
                if col > 0:
                    col -= 1
            if direction == "R":
                if col < 2:
                    col += 1
            if direction == "U":
                if row > 0:
                    row -= 1
            if direction == "D":
                if row < 2:
                    row += 1

        # when the directions for a line are done, record what button you landed on
        code.append(keypad[row][col])
    
    return code

def part2(directions):
    # setup the bathroom lock
    keypad = [[0,0,1,0,0],[0,2,3,4,0],[5,6,7,8,9],[0,'A','B','C',0],[0,0,'D',0,0]]

    # starting key is 5, set up our code list: 
    row, col, code = 2, 0, [] 

    # move and record
    for line in directions:
        
        # move; go thru all the directions for the line
        for direction in line:
            if direction == "L":
                if row == 0 or row == 4:
                    pass
                if (row == 1 or row == 3) and col > 1:
                    col -= 1
                if row == 2 and col > 0:
                    col -= 1    
            if direction == "R":
                if row == 0 or row == 4:
                    pass
                if (row == 1 or row == 3) and col < 3:
                    col += 1
                if row == 2 and col < 4:
                    col += 1

            if direction == "U":
                if col == 0 or col == 4:
                    pass
                if (col == 1 or col == 3) and row > 1:
                    row -= 1
                if col == 2 and row > 0:
                    row -= 1
            if direction == "D":
                if col == 0 or col == 4:
                    pass
                if (col == 1 or col == 3) and row < 3:
                    row += 1
                if col == 2 and row < 4:
                    row += 1

        # when the directions for a line are done, record what button you landed on
        code.append(keypad[row][col])
    
    return code


print(part1(directions))
print(part2(directions))

