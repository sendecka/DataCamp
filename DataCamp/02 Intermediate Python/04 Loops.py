### Basic while loop
# Instructions
# Create the variable offset with an initial value of 8.
# Code a while loop that keeps running as long as offset is not equal to 0. Inside the while loop:
# Print out the sentence "correcting...".
# Next, decrease the value of offset by 1. You can do this with offset = offset - 1.
# Finally, still within your loop, print out offset so you can see how it changes.

# Initialize offset
offset = 8

# Code the while loop
while offset != 0:
    print("correcting...")
    offset = offset - 1
    print(offset)


### Add conditionals
# Instructions
# Inside the while loop, complete the if-else statement:
# If offset is greater than zero, you should decrease offset by 1.
# Else, you should increase offset by 1.
# If you've coded things correctly, hitting Submit Answer should work this time.
# If your code is still taking too long to run (or your session is expiring), you probably made a mistake. Check your code and make sure that the statement offset != 0 will eventually evaluate to FALSE!

# Initialize offset
offset = -6

# Code the while loop
while offset != 0:
    print("correcting...")
    if offset > 0:
        offset = offset - 1
    else:
        offset = offset + 1
    print(offset)


### Loop over a list
# Instructions
# Write a for loop that iterates over all elements of the areas list and prints out every element separately.

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for area in areas:
    print(area)


### Indexes and values (1)
# Instructions
# Adapt the for loop in the sample code to use enumerate() and use two iterator variables.
# Update the print() statement so that on each run, a line of the form "room x: y" should be printed, where x is the index of the list element and y is the actual list element, i.e. the area. Make sure to print out this exact string, with the correct spacing.

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index, area in enumerate(areas):
    print("room " + str(index) + ": " + str(area))



### Indexes and values (21)
# Instructions
# Adapt the print() function in the for loop so that the first printout becomes "room 1: 11.25", the second one "room 2: 18.0" and so on.

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for index, area in enumerate(areas):
    print("room " + str(index + 1) + ": " + str(area))



### Loop over list of lists
# Instructions
# Write a for loop that goes through each sublist of house and prints out the x is y sqm, where x is the name of the room and y is the area of the room.

# house list of lists
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
for room, areas in house:
    print("the " + str(room) + " is " + str(areas) + " sqm")


### Loop over dictionary
# Instructions
# Write a for loop that goes through each key:value pair of europe. On each iteration, "the capital of x is y" should be printed out, where x is the key and y is the value of the pair.

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for key, value in europe.items():
    print("the capital of " + str(key) + " is " + str(value))


### Loop over NumPy array
# Instructions
# Import the numpy package under the local alias np.
# Write a for loop that iterates over all elements in np_height and prints out "x inches" for each element, where x is the value in the array.
# Write a for loop that visits every element of the np_baseball array and prints it out.

# Import numpy as np
import numpy as np

# For loop over np_height
for height in np_height:
    print(str(height) + " inches")

# For loop over np_baseball
for mesures in np.nditer(np_baseball):
    print(mesures)


### Loop over DataFrame (1)
# Instructions
# Write a for loop that iterates over the rows of cars and on each iteration perform two print() calls: one to print out the row label and one to print out all of the rows contents.

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, row in cars.iterrows():
    print(lab)
    print(row)



### Loop over DataFrame (2)
# Instructions
# Using the iterators lab and row, adapt the code in the for loop such that the first iteration prints out "US: 809", the second iteration "AUS: 731", and so on.
# The output should be in the form "country: cars_per_cap". Make sure to print out this exact string (with the correct spacing).
# You can use str() to convert your integer data to a string so that you can print it in conjunction with the country label.

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop
for lab, row in cars.iterrows():
    print(lab + ": " + str(row["cars_per_cap"]))



### Add column (1)
# Instructions
# Use a for loop to add a new column, named COUNTRY, that contains a uppercase version of the country names in the "country" column. You can use the string method upper() for this.
# To see if your code worked, print out cars. Don't indent this code, so that it's not part of the for loop.

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows():
    cars.loc[lab, "COUNTRY"] = row["country"].upper()


# Print cars
print(cars)



### Add column (2)
# Instructions
# Replace the for loop with a one-liner that uses .apply(str.upper). The call should give the same result: a column COUNTRY should be added to cars, containing an uppercase version of the country names.
# As usual, print out cars to see the fruits of your hard labor

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)