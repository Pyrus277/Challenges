
# See day1-rationale.md for a breakdown of the problem solving approach.

# Read in and setup the data as a list:
with open('day1.txt') as fhand:
    document = fhand.read().splitlines() 
document = document[0].split(", ")

direction = 'N' # starting direction
x, y = 0, 0 # starting grid location


# Update the current facing direction using the L/R part for each item in the list...
def new_dir(direction, rotate):
    '''
    direction = current facing direction
    rotate = L or R based on the charater part of the input string
    '''    
    result= {'L':{'N':'W', 'S':'E', 'E':'N', 'W':'S'},
            'R':{'N':'E', 'S':'W', 'E':'S', 'W':'N'}}
    return result[rotate][direction]

# Then update x or y based on the new direction we found with new_dir() and also the integer part of the input
def movement(direction, move, x, y):
    '''
    direction = current facing direction
    move = integer, how many spaces forward moved in the current facing direction
    '''
    if direction == "W": 
        x -= move
        return x, y
    if direction == "E":
        x += move
        return x, y
    if direction == "N":
        y += move
        return x, y
    if direction == "S":
        y -= move
        return x, y

# For part 2-- determine if we hit a location we've been to before, and if so, end travel there
def mk_tups(start, dest, const, axis, locations, dup=False):
    '''
    This function generates tuples representing the ordered pairs for locations
    visited during travel on the grid.

    start = x or y; int from the ordered pair of the start location
    dest = x_dest or y_dest; int from the ordered pair of the dest location
    cons = current value of the axis we are not moving along
    locations = set of ordered pairs for locations we have been to 

    If we do not detect the tuple for a location we have been to, this returns
    x_dest and y_dest as the current x and y for the next iteration.

    If we do encounter a repeat tuple, we return x and y for that location, 
    along with a flag to break the loop and do the final distance calculation
    with that x y pair.
    '''
    if dest < start: # we need to decrement range so the location encounter order is correct.
        for i in range(start-1, dest-1, -1):
            if axis == 'X':
                if (i,const) in locations:
                    x_dest, y_dest, dup = i, const, True
                    break
                locations.add((i, const))
                x_dest, y_dest, dup = i, const, False
            if axis == 'Y':
                if (const, i) in locations:
                    x_dest, y_dest, dup = const, i, True
                    break
                locations.add((const, i))
                x_dest, y_dest, dup = const, i, False
    else:
        for i in range(start+1, dest+1):
            if axis == 'X':
                if (i,const) in locations:
                    x_dest, y_dest, dup = i, const, True
                    break
                locations.add((i, const))
                x_dest, y_dest, dup = i, const, False
            if axis == 'Y':
                if (const, i) in locations:
                    x_dest, y_dest, dup = const, i, True
                    break
                locations.add((const, i))
                x_dest, y_dest, dup = const, i, False

    return x_dest, y_dest, locations, dup  


# Main functions
#   Part 1 returns the distance from origin traveled by following the entire document
def part1(document, direction, x, y):
    # iterate through the input list
    for i in document:
        direction = new_dir(direction, i[0])
        x, y = movement(direction, int(i[1:]), x, y)
    return abs(x)+abs(y)

#   Part 2 returns the distance from origin traveled by following the document to the end
#       or until we hit a location we have already been to. 
def part2(document, direction, x, y):
    dup = False
    locations = {(0,0)}
    for i in document:
        direction = new_dir(direction, i[0]) # get the new facing direction
        x_dest, y_dest = movement(direction, int(i[1:]), x, y) # get x,y for the destination
        # New part: check for a dup location along this path. If we find one, 
        # stop the iteration and make this location the final x and y.
        if abs((x_dest - x)) > 0: # if we moved on the x axis
            x, y, locations, dup = mk_tups(x, x_dest, y, 'X', locations)
        if abs((y_dest - y)) > 0: # if we moved on the y axis
            x, y, locations, dup = mk_tups(y, y_dest, x, 'Y', locations) 
        
        if dup is True: # if we've been to the same location, end the loop.
            break
    return abs(x)+abs(y)

# Output
print("Part 1: ", part1(document, direction, x, y))
print("Part 2: ", part2(document, direction, x, y))



