# Advent of Code 2016: Day 1


## Part 1 Premise:
Your character will start at location (0,0), facing north, on an evenly spaced grid.  
After following a set of directions, the input, the character will end at spot (x,y)  
How many grid blocks away from the starting location does the character end up?  

## Part 1 Solution:
The ending location distance can be found by the Manhattan distance formula:  
|x1-x2| + |y1-y2|.  
Since the starting location is (0,0), the distance in blocks traveled is:  
|0-x| + |0-y| or simply, x + y

In other words, there is going to be an overall distance traveled along the x-axis,
and likewise over the y-axis. How can we find these distances with the input like
"R5 L5 R5 R3" to get the total distance traveled?

For any given starting direction in which the character faces on a leg of the trip, a left rotation L or right rotation R will result in a new facing direction:
|Starting Direction|Rotation|**New Direction**|
|---|---|---|
|N|L|**W**|
|S|L|**E**|
|E|L|**N**|
|W|L|**S**|
|N|R|**W**|
|S|R|**E**|
|E|R|**N**|
|W|R|**S**|

*Code: This table can be stored as a dictionary, and it can be used in a function to find the new facing direction based on start direction and rotation* 

The new direction before the movement will then determine movement along the x or y axis:
|New Direction|Movement|**Axis Position Change**|
|---|---|---|
|W|5|**x = x - movement**|
|E|5|**x = x + movement**|
|N|5|**y = y + movement**|
|S|3|**y = y - movement**|
  

## Part 1 Test Case Solution Summary
Again, our sample data is: "R5 L5 R5 R3"

We can summarize the solution to the problem with the following table:
|Input|Direction|Rotation|**New Direction**|**Axis Position Change**|x|y|
|---|---|---|---|---|---|---|
|(start)|N|-|-|-|0|0|
|R5|N|R|**E**|**x=y+5**|5|0|
|L5|E|L|**N**|**y=y+5**|5|5|
|R5|N|R|**E**|**x=x+5**|10|5|
|L3|E|R|**S**|**y=y-3**|**10**|**2**| 

With a final x,y position of (10,2), the total distance traveled from the origin is  
|0-10| + |0-2| = 10 + 2 = **12**
  
    
## Part 2 Premise:
The same as part one, but with the modification that if we encounter a given grid position more than once, that positon is our actual destination and travel ends. 
**Note:** this doesn't just consider revisiting the endpoint of a leg of the trip; even if we encounter a point we've been to mid-leg, travel ends there. 
  
## Part 2 Solution:
Same as above, but additionally, for each leg of the trip, consider its starting point and ending point.  
Depending on which axis we're moving on, hold the other one constant and generate tuples for this range representing the points visited.  
As we generate the tuples, add them to a set.  
If we would add a tuple that already exists in the set, set x and y to be the values of this tuple and break the loop. 
It's important to generate these tuples in the order encountered, so the first duplicate encountered is the one we collect the final x and y values for. 

For the example "R8, R4, R4, R8" we can summarize 
Input|~|location tuples|x|y|
|---|---|---|---|---|
|(start)|~||0|0|
|R8|~|(1,0), (2,0), (3,0), **(4,0)**, (5,0), (6,0), (7,0), (8,0)|8|0|
|R4|~|(8,-1), (8,-2), (8,-3), (8,-4)|8|-4|
|R4|~|(7,-4), (6,-4), (5,-4), (4,-4)|4|-4|
|R8|~|(4,-3), (4,-2), (4,-1), **(4,0)** stop!|4|0|

We see that in the middle of the R8 leg of the trip, we encounter (4,0) which we already saw on the first leg of the trip (R8)
This will be set as the final x and y, and as above, we get our final distance from origin like:
|0-4| + |0-0| = 4 + 0 = **4**