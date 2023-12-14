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


### Python as a calculator
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


### Variable Assignment
# Instructions:
# Create a variable savings with the value of 100.
# Check out this variable by typing print(savings) in the script. 

# Create a variable savings
savings = 100

# Print out savings
print(savings)


### Calculations with variables
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


### Other variable types
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


### Operations with other types
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

### Type conversion
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