### Line plot (1)
# Instructions
# print() the last item from both the year and the pop list to see what the predicted population for the year 2100 is. Use two print() functions.
# Before you can start, you should import matplotlib.pyplot as plt. pyplot is a sub-package of matplotlib, hence the dot.
# Use plt.plot() to build a line plot. year should be mapped on the horizontal axis, pop on the vertical axis. Don't forget to finish off with the plt.show() function to actually display the plot.

# Print the last item from year and pop
print(year[-1])
print(pop[-1])


# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt


# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year,pop)


# Display the plot with plt.show()
plt.show()


# Line Plot (2): Interpretation
# Instructions
# Print the last item from both the list gdp_cap, and the list life_exp; it is information about Zimbabwe.
# Build a line chart, with gdp_cap on the x-axis, and life_exp on the y-axis. Does it make sense to plot this data on a line plot?
# Don't forget to finish off with a plt.show() command, to actually display the plot.

# Print the last item of gdp_cap and life_exp
print(gdp_cap[-1])
print(life_exp[-1])


# Make a line plot, gdp_cap on the x-axis, life_exp on the y-axis
plt.plot(gdp_cap, life_exp)

# Display the plot
plt.show()

# Scatter Plot (1)
# Instructions
# Change the line plot that's coded in the script to a scatter plot.
# A correlation will become clear when you display the GDP per capita on a logarithmic scale. Add the line plt.xscale('log').
# Finish off your script with plt.show() to display the plot.

# Change the line plot below to a scatter plot
plt.scatter(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale
plt.xscale('log')

# Show plot
plt.show()

# Scatter plot (2)
# Instructions
# Start from scratch: import matplotlib.pyplot as plt.
# Build a scatter plot, where pop is mapped on the horizontal axis, and life_exp is mapped on the vertical axis.
# Finish the script with plt.show() to actually display the plot. Do you see a correlation?

# Import package
import matplotlib.pyplot as plt

# Build Scatter plot
plt.scatter(pop, life_exp)

# Show plot
plt.show()

# Build a histogram (1)
# Instructions
# Use plt.hist() to create a histogram of the values in life_exp. Do not specify the number of bins; Python will set the number of bins to 10 by default for you.
# Add plt.show() to actually display the histogram. Can you tell which bin contains the most observations?

# Create histogram of life_exp data
plt.hist(life_exp)

# Display histogram
plt.show()

# Build a histogram (2): bins
# Instructions
# Build a histogram of life_exp, with 5 bins. Can you tell which bin contains the most observations?
# Build another histogram of life_exp, this time with 20 bins. Is this better?

# Build histogram with 5 bins
plt.hist(life_exp, bins=5)

# Show and clean up plot
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist(life_exp, bins=20)

# Show and clean up again
plt.show()
plt.clf()

### Build a histogram (3): compare
# Instructions
# Build a histogram of life_exp with 15 bins.
# Build a histogram of life_exp1950, also with 15 bins. Is there a big difference with the histogram for the 2007 data?

# Histogram of life_exp, 15 bins
plt.hist(life_exp, bins=15)

# Show and clear plot
plt.show()
plt.clf()

# Histogram of life_exp1950, 15 bins
plt.hist(life_exp1950, bins=15)

# Show and clear plot again
plt.show()
plt.clf()

### Labels
# Instructions
# The strings xlab and ylab are already set for you. Use these variables to set the label of the x- and y-axis.
# The string title is also coded for you. Use it to add a title to the plot.
# After these customizations, finish the script with plt.show() to actually display the plot.

# Basic scatter plot, log scale
plt.scatter(gdp_cap, life_exp)
plt.xscale('log') 

# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)

# Add title
plt.title(title)

# After customizing, display the plot
plt.show()

### Ticks
# Instructions
# Use tick_val and tick_lab as inputs to the xticks() function to make the the plot more readable.
# As usual, display the plot with plt.show() after you've added the customizations.

# Scatter plot
plt.scatter(gdp_cap, life_exp)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')

# Definition of tick_val and tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

# Adapt the ticks on the x-axis
plt.xticks([1000, 10000, 100000], ['1k', '10k', '100k'])

# After customizing, display the plot
plt.show()


### Sizes
# Instructions
# Run the script to see how the plot changes.
# Looks good, but increasing the size of the bubbles will make things stand out more.
# Import the numpy package as np.
# Use np.array() to create a numpy array from the list pop. Call this NumPy array np_pop.
# Double the values in np_pop setting the value of np_pop equal to np_pop * 2. Because np_pop is a NumPy array, each array element will be doubled.
# Change the s argument inside plt.scatter() to be np_pop instead of pop.

# Import numpy as np
import numpy as np

# Store pop as a numpy array: np_pop
np_pop = np.array(pop)

# Double np_pop
np_pop = np_pop * 2

# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = np_pop)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()


### Colors
# Instructions
# Add c = col to the arguments of the plt.scatter() function.
# Change the opacity of the bubbles by setting the alpha argument to 0.8 inside plt.scatter(). Alpha can be set from zero to one, where zero is totally transparent, and one is not at all transparent.

# Specify c and alpha inside plt.scatter()
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Show the plot
plt.show()


### Additional Customizations
# Instructions
# Add plt.grid(True) after the plt.text() calls so that gridlines are drawn on the plot.

# Scatter plot
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Additional customizations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

# Add grid() call
plt.grid(True)

# Show the plot
plt.show()




