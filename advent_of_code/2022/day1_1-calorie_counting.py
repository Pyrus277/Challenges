# AOC Day 1 - Part 1

'''
1. Read txt file without new lines 
2. Newlines will be '', convert these to zeroes
3. Map the strings into ints
    https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
4. Break the list by the 0 into sublists with numpy
    https://www.geeksforgeeks.org/python-split-list-into-lists-by-particular-value/
5. Sum the sublists and max the main list for the solution. 
'''
import numpy as np

with open("day1.txt") as f:
    calories = f.read().splitlines() # read in data without the newline chars

calories = list(map(lambda x: 0 if x=='' else x, calories)) # turn the ''s into 0 so we can...
calories = list(map(int,calories)) # ...convert strings to ints without error

splitval = 0 # 0s indicate the grouping breaks
calories = np.array(calories) 
idx = np.where(calories == splitval)[0] # get the indices where the value in calories == 0.

calories = np.split(calories, idx+1) # split the array into subarrays using np.split

# sum the sunarrays and print the max value
elves = []
for elf in calories:
    elves.append(elf.sum())
print(max(elves))


