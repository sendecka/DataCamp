### Equality
# Instructions
# In the editor on the right, write code to see if True equals False.
# Write Python code to check if -5 * 15 is not equal to 75.
# Ask Python whether the strings "pyscript" and "PyScript" are equal.
# What happens if you compare booleans and integers? Write code to see if True and 1 are equal.

# Comparison of booleans
True == False

# Comparison of integers
-5 * 15 != 75

# Comparison of strings
'pyscript' == 'PyScript'

# Compare a boolean with an integer
True == 1

### Greater and less than
# Instructions
# Write Python expressions, wrapped in a print() function, to check whether:
# x is greater than or equal to -10. x has already been defined for you.
# "test" is less than or equal to y. y has already been defined for you.
# True is greater than False.

# Comparison of integers
x = -3 * 6
print(x >= -10)

# Comparison of strings
y = "test"
print('test' <= y)

# Comparison of booleans
print(True > False)


### Compare arrays
# Instructions
# Using comparison operators, generate boolean arrays that answer the following questions:
# Which areas in my_house are greater than or equal to 18?
# You can also compare two NumPy arrays element-wise. Which areas in my_house are smaller than the ones in your_house?
# Make sure to wrap both commands in a print() statement so that you can inspect the output!

# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18
print(my_house >= 18)

# my_house less than your_house
print(my_house < your_house)



### and, or, not (1)
# Instructions
# Write Python expressions, wrapped in a print() function, to check whether:
# my_kitchen is bigger than 10 and smaller than 18.
# my_kitchen is smaller than 14 or bigger than 17.
# double the area of my_kitchen is smaller than triple the area of your_kitchen.

# Define variables
my_kitchen = 18.0
your_kitchen = 14.0

# my_kitchen bigger than 10 and smaller than 18?
print(my_kitchen > 10 and my_kitchen < 18)

# my_kitchen smaller than 14 or bigger than 17?
print(my_kitchen < 14 or my_kitchen > 17)

# Double my_kitchen smaller than triple your_kitchen?
print(my_kitchen * 2 < your_kitchen * 3)



### Boolean operators with NumPy
# Instructions
# Generate boolean arrays that answer the following questions:
# Which areas in my_house are greater than 18.5 or smaller than 10?
# Which areas are smaller than 11 in both my_house and your_house? Make sure to wrap both commands in print() statement, so that you can inspect the output.

# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house > 18.5, my_house < 10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house < 11, your_house < 11))



### if
# Instructions
# Examine the if statement that prints out "looking around in the kitchen." if room equals "kit".
# Write another if statement that prints out "big place!" if area is greater than 15.

# Define variables
room = "kit"
area = 14.0

# if statement for room
if room == "kit" :
    print("looking around in the kitchen.")

# if statement for area
if area > 15 :
    print("big place!")

### Add else
# Instructions
# Add an else statement to the second control structure so that "pretty small." is printed out if area > 15 evaluates to False.

# Define variables
room = "kit"
area = 14.0

# if-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
else :
    print("looking around elsewhere.")

# if-else construct for area
if area > 15 :
    print("big place!")
else :
    print('pretty small.')


### Customize further: elif
# Instructions
# Add an elif to the second control structure such that "medium size, nice!" is printed out if area is greater than 10.

# Define variables
room = "bed"
area = 14.0

# if-elif-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else :
    print("looking around elsewhere.")

# if-elif-else construct for area
if area > 15 :
    print("big place!")
elif area > 10 :
    print('medium size, nice!')
else :
    print("pretty small.")



### Driving right (1)
# Instructions
# Extract the drives_right column as a Pandas Series and store it as dr.
# Use dr, a boolean Series, to subset the cars DataFrame. Store the resulting selection in sel.
# Print sel, and assert that drives_right is True for all observations.

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Extract drives_right column as Series: dr
dr = cars["drives_right"]

# Use dr to subset cars: sel
sel = cars[dr]

# Print sel
print(sel)


### Driving right (2)
# Instructions
# Convert the code to a one-liner that calculates the variable sel as before.

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Convert code to a one-liner
sel = cars[cars['drives_right']]

# Print sel
print(sel)



### Cars per capita (1)
# Instructions
# Select the cars_per_cap column from cars as a Pandas Series and store it as cpc.
# Use cpc in combination with a comparison operator and 500. You want to end up with a boolean Series that's True if the corresponding country has a cars_per_cap of more than 500 and False otherwise. Store this boolean Series as many_cars.
# Use many_cars to subset cars, similar to what you did before. Store the result as car_maniac.
# Print out car_maniac to see if you got it right.

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars["cars_per_cap"]
many_cars = cpc > 500
car_maniac = cars[many_cars]



# Print car_maniac
print(car_maniac)



### Cars per capita (2)
# Instructions
# Use the code sample provided to create a DataFrame medium, that includes all the observations of cars that have a cars_per_cap between 100 and 500.
# Print out medium.

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Import numpy, you'll need this
import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500
medium = cars[np.logical_and(cars["cars_per_cap"] > 100, cars["cars_per_cap"] < 500)]

# Print medium
print(medium)

