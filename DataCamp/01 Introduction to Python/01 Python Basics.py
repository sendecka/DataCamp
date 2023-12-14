### The Python Interface

# Instructions:
# Experiment in the IPython Shell; type 5 / 8, for example.
# Add another line of code to script.py, print(7 + 10), to be checked for correctness.
# Hit Submit Answer to execute the Python script and receive feedback.

# Example, do not modify!
print(5 / 8)

# Print the sum of 7 and 10
print(7 + 10)


# Instructions:
# Above the print(7 + 10), add the comment

# Testing Division
print(5 / 8)

# Addition
print(7 + 10)


# Instructions:
# Print the sum of 4 + 5.
# Print the result of subtracting 5 from 5.
# Print the result of multiplying 3 by 5.
# Print the result of dividing 10 by 2.

# Addition
print(4 + 5)

# Subtraction
print(5 - 5)

# Multiplication
print(3 * 5)

# Division
print(10 / 2) 


# Instructions:
# Create a variable savings with the value of 100.
# Check out this variable by typing print(savings) in the script. 

# Create a variable savings
savings = 100

# Print out savings
print(savings)


# Instructions:
# Create a variable monthly_savings, equal to 10 and num_months, equal to 4.
# Multiply monthly_savings by num_months and save it to new_savings.
# Add new_savings to savings, saving the sum as total_savings.
# Print the value of total_savings.

# Create the variables monthly_savings and num_months
monthly_savings = 10
num_months = 4

# Multiply monthly_savings and num_months
new_savings = monthly_savings * num_months

# Add new_savings to your savings
total_savings = new_savings + savings

# Print total_savings
print(total_savings)


# Instructions:
# Create a new float, half, with the value 0.5.
# Create a new string, intro, with the value "Hello! How are you?".
# Create a new boolean, is_good, with the value True.

# Create a variable half
half = 0.5

# Create a variable intro
intro = "Hello! How are you?"

# Create a variable is_good
is_good = True


# Instructions:
# Calculate the product of monthly_savings and num_months. Store the result in year_savings.
# What do you think the resulting type will be? Find out by printing out the type of year_savings.
# Calculate the sum of intro and intro and store the result in a new variable doubleintro.
# Print out doubleintro. Did you expect this?

monthly_savings = 10
num_months = 12
intro = "Hello! How are you?"

# Calculate year_savings using monthly_savings and num_months
year_savings = monthly_savings * num_months

# Print the type of year_savings
print(type(year_savings))

# Assign sum of intro and intro to doubleintro
doubleintro = intro + intro

# Print out doubleintro
print(doubleintro)


# Instructions:
# Hit Run Code to run the code. Try to understand the error message.
# Fix the code such that the printout runs without errors; use the function str() to convert the variables savings and total_savings to strings.
# Convert the variable pi_string to a float and store this float as a new variable, pi_float.

# Definition of savings and total_savings
savings = 100
total_savings = 150

# Fix the printout
print("I started with $" + str(savings) + " and now have $" + str(total_savings) + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
pi_float = float(pi_string)


# Instructions:
# Create a list, areas, that contains the area of the hallway (hall), kitchen (kit), living room (liv), bedroom (bed) and bathroom (bath), in this order. Use the predefined variables.
# Print areas with the print() function.

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]

# Print areas
print(areas)


# Instructions:
# Finish the code that creates the areas list. Build the list so that the list first contains the name of each room as a string and then its area. In other words, add the strings "hallway", "kitchen" and "bedroom" at the appropriate locations.
# Print areas again; is the printout more informative this time?

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print areas
print(areas)


# Instructions:
# Finish the list of lists so that it also contains the bedroom and bathroom data. Make sure you enter these in order!
# Print out house; does this way of structuring your data make more sense?
# Print out the type of house. Are you still dealing with a list?

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)

# Print out the type of house
print(type(house))


### Subset and conquer
# Instructions:
# Print out the second element from the areas list (it has the value 11.25).
# Subset and print out the last element of areas, being 9.50. Using a negative index makes sense here!
# Select the number representing the area of the living room (20.0) and print it out.

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])

### Subset and calculate
# Instructions:
# Using a combination of list subsetting and variable assignment, create a new variable, eat_sleep_area, that contains the sum of the area of the kitchen and the area of the bedroom.
# Print the new variable eat_sleep_area.

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area = areas[3] + areas[-3]

# Print the variable eat_sleep_area
print(eat_sleep_area)


### Slicing and dicing
# Instructions:
# Use slicing to create a list, downstairs, that contains the first 6 elements of areas.
# Do a similar thing to create a new variable, upstairs, that contains the last 4 elements of areas.
# Print both downstairs and upstairs using print().

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[0:6]

# Use slicing to create upstairs
upstairs = areas[6:10]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)


### Slicing and dicing (2)
# Instructions:
# Create downstairs again, as the first 6 elements of areas. This time, simplify the slicing by omitting the begin index.
# Create upstairs again, as the last 4 elements of areas. This time, simplify the slicing by omitting the end index.

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Alternative slicing to create downstairs
downstairs = areas[ :6]

# Alternative slicing to create upstairs
upstairs = areas[6: ]


### Replace list elements
# Instructions:
# Update the area of the bathroom area to be 10.50 square meters instead of 9.50.
# Make the areas list more trendy! Change "living room" to "chill zone".

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4] = "chill zone"


### Extend a list
# Instructions:
# Use the + operator to paste the list ["poolhouse", 24.5] to the end of the areas list. Store the resulting list as areas_1.
# Further extend areas_1 by adding data on your garage. Add the string "garage" and float 15.45. Name the resulting list areas_2.

# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]


### Inner workings of lists
# Instructions:
# Change the second command, that creates the variable areas_copy, such that areas_copy is an explicit copy of areas. After your edit, changes made to areas_copy shouldn't affect areas. Submit the answer to check this.

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)


### Familiar functions
# Instructions:
# Use print() in combination with type() to print out the type of var1.
# Use len() to get the length of the list var1. Wrap it in a print() call to directly print it out.
# Use int() to convert var2 to an integer. Store the output as out2.

# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)


### Multiple arguments
# Instructions:
# Use + to merge the contents of first and second into a new list: full.
# Call sorted() on full and specify the reverse argument to be True. Save the sorted list as full_sorted.
# Finish off by printing out full_sorted.

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)

# Print out full_sorted
print(full_sorted)


### String Methods
# Instructions:
# Use the upper() method on place and store the result in place_up. Use the syntax for calling methods that you learned in the previous video.
# Print out place and place_up. Did both change?
# Print out the number of o's on the variable place by calling count() on place and passing the letter 'o' as an input to the method. We're talking about the variable place, not the word "place"!

# string to experiment with: place
place = "poolhouse"

# Use upper() on place: place_up
place_up = str.upper(place)

# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place
print(place.count)


### List Methods
# Instructions:
# Use the index() method to get the index of the element in areas that is equal to 20.0. Print out this index.
# Call count() on areas to find out how many times 9.50 appears in the list. Again, simply print out this number.

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))


### List Methods (2)
# Instructions:
# Use append() twice to add the size of the poolhouse and the garage again: 24.5 and 15.45, respectively. Make sure to add them in this order.
# Print out areas
# Use the reverse() method to reverse the order of the elements in areas.
# Print out areas once more.

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)


### Import package
# Instructions:
# Import the math package. Now you can access the constant pi with math.pi.
# Calculate the circumference of the circle and store it in C.
# Calculate the area of the circle and store it in A.

# Import the math package
import math

# Definition of radius
r = 0.43
pi = math.pi

# Calculate C
C = 2 * pi * r

# Calculate A
A = pi * r * r

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))

### Selective import
# Instructions:
# Perform a selective import from the math package where you only import the radians function.
# Calculate the distance travelled by the Moon over 12 degrees of its orbit. Assign the result to dist. You can calculate this as r * phi, where r is the radius and phi is the angle in radians. To convert an angle in degrees to an angle in radians, use the radians() function, which you just imported.
# Print out dist.

# Import radians function of math package
from math import radians

# Definition of radius
r = 192500

# Travel distance of Moon over 12 degrees. Store in dist.
dist = radians(r * 12)

# Print out dist
print(dist)


### Your First NumPy Array
# Instructions:
# Import the numpy package as np, so that you can refer to numpy with np.
# Use np.array() to create a numpy array from baseball. Name this array np_baseball.
# Print out the type of np_baseball to check that you got it right.

# Import the numpy package as np
import numpy as np

# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))


### Baseball players' height
# Instructions:
# Create a numpy array from height_in. Name this new array np_height_in.
# Print np_height_in.
# Multiply np_height_in with 0.0254 to convert all height measurements from inches to meters. Store the new values in a new array, np_height_m.
# Print out np_height_m and check if the output makes sense.