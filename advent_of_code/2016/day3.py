# Advent of Code 2016 Day 3
# https://adventofcode.com/2016/day/3

# bring in and wrangle in the data
triangles = []
with open('day3.txt') as fhand:
    document = fhand.read().splitlines() 
    for line in document:
        triangles.append(line)
# we got three columns of numbers, and the whitespace between them varies, so:
for i, x in enumerate(triangles):
    triangles[i] = x.split() # giving no parameter will split on any amount of whitespace
    triangles[i] = [int(x) for x in triangles[i]] # we need ints!


def part_1(triangles):

    def valid_triangle(tri):
        if tri[0] + tri[1] <= tri[2] or \
            tri[0] + tri[2] <= tri[1] or \
            tri[1] + tri[2] <= tri[0]:
            return False
        else:
            return True

    count = 0

    for tri in triangles:
        if valid_triangle(tri):
            count += 1

    return count


def part2(triangles):
    pass

    # this part looks like you might want to break out numpy or pandas!

print(part_1(triangles))


