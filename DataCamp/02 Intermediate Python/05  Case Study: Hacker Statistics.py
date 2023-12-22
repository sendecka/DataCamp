### Random float
# Instructions
# Import numpy as np.
# Use seed() to set the seed; as an argument, pass 123.
# Generate your first random float with rand() and print it out.

# Import numpy as np
import numpy as np


# Set the seed
np.random.seed(123)

# Generate and print random float
print(np.random.rand())



### Roll the dice
# Instructions
# Use randint() with the appropriate arguments to randomly generate the integer 1, 2, 3, 4, 5 or 6. This simulates a dice. Print it out.
# Repeat the outcome to see if the second throw is different. Again, print out the result.

# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Use randint() to simulate a dice
print(np.random.randint(1, 7))

# Use randiprint(np.random.randint(1, 7))nt() again
print(np.random.randint(1, 7))



### Determine your next move
# Instructions
# Roll the dice. Use randint() to create the variable dice.
# Finish the if-elif-else construct by replacing ___:
# If dice is 1 or 2, you go one step down.
# if dice is 3, 4 or 5, you go one step up.
# Else, you throw the dice again. The number on the dice is the number of steps you go up.
# Print out dice and step. Given the value of dice, was step updated correctly?

# NumPy is imported, seed is set

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1, 7)

# Finish the control construct
if dice <= 2:
    step = step - 1
elif dice <= 5:
    step = step + 1
else:
    step = step + np.random.randint(1, 7)

# Print out dice and step
print(dice)
print(step)


### The next step
# Instructions
# Make a list random_walk that contains the first step, which is the integer 0.
# Finish the for loop:
# The loop should run 100 times.
# On each iteration, set step equal to the last element in the random_walk list. You can use the index -1 for this.
# Next, let the if-elif-else construct update step for you.
# The code that appends step to random_walk is already coded.
# Print out random_walk.

# NumPy is imported, seed is set

# Initialize random_walk
random_walk = [0]

# Complete the ___
for x in range(100):
# Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1, 7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)


### How low can you go?
# Instructions
# Use max() in a similar way to make sure that step doesn't go below zero if dice <= 2.
# Hit Submit Answer and check the contents of random_walk.

# NumPy is imported, seed is set

# Initialize random_walk
random_walk = [0]

for x in range(100):
    step = random_walk[-1]
    dice = np.random.randint(1, 7)

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1, 7)

    random_walk.append(step)


### Visualize the walk
# Instructions
# Add some lines of code after the for loop:
# Import matplotlib.pyplot as plt.
# Use plt.plot() to plot random_walk.
# Finish off with plt.show() to actually display the plot.

# NumPy is imported, seed is set

# Initialization
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)

# Show the plot
plt.show()



### Simulate multiple walks
# Instructions
# Fill in the specification of the for loop so that the random walk is simulated five times.
# After the random_walk array is entirely populated, append the array to the all_walks list.
# Finally, after the top-level for loop, print out all_walks.

# NumPy is imported; seed is set

# Initialize all_walks (don't change this line)
all_walks = []

# Simulate random walk five times
for i in range(5):

    # Code from before
    random_walk = [0]
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1, 7)
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)

# Print all_walks
print(all_walks)



### Implement clumsiness
# Instructions
# Change the range() function so that the simulation is performed 20 times.
# Finish the if condition so that step is set to 0 if a random float is less or equal to 0.005. Use np.random.rand().

# numpy and matplotlib imported, seed set

# clear the plot so it doesn't get cluttered if you run this many times
plt.clf()

# Simulate random walk 20 times
all_walks = []
for i in range(20) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        # Implement clumsiness
        if np.random.rand() <= 0.005 :
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show()



### Plot the distribution
# Instructions
# To make sure we've got enough simulations, go crazy. Simulate the random walk 500 times.
# From np_aw_t, select the last row. This contains the endpoint of all 500 random walks you've simulated. Store this NumPy array as ends.
# Use plt.hist() to build a histogram of ends. Don't forget plt.show() to display the plot.

# numpy and matplotlib imported, seed set

# Simulate random walk 500 times
all_walks = []
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1, :]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()