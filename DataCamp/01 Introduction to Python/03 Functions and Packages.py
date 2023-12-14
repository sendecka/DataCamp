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

# Import numpy
import numpy as np

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m = np_height_in * 0.0254

# Print np_height_m
print(np_height_m)


### Baseball player's BMI
# Instructions:
# Create a numpy array from the weight_lb list with the correct units. Multiply by 0.453592 to go from pounds to kilograms. Store the resulting numpy array as np_weight_kg.
# Use np_height_m and np_weight_kg to calculate the BMI of each player. Use the following equation:
 
# Save the resulting numpy array as bmi.
# Print out bmi.

# Import numpy
import numpy as np

# Create array from height_in with metric units: np_height_m
np_height_m = np.array(height_in) * 0.0254

# Create array from weight_lb with metric units: np_weight_kg
np_weight_kg = np.array(weight_lb) * 0.453592

# Calculate the BMI: bmi
bmi = np_weight_kg / np_height_m**2

# Print out bmi
print(bmi)