### Motivation for dictionaries
# Instructions
# Use the index() method on countries to find the index of 'germany'. Store this index as ind_ger.
# Use ind_ger to access the capital of Germany from the capitals list. Print it out.

# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger = countries.index("germany")

# Use ind_ger to print out capital of Germany
print(capitals[ind_ger])


### Create dictionary
# Instructions
# With the strings in countries and capitals, create a dictionary called europe with 4 key:value pairs. Beware of capitalization! Make sure you use lowercase characters everywhere.
# Print out europe to see

# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# From string in countries and capitals, create dictionary europe
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo'}

# Print europe
print(europe)


### Access dictionary
# Instructions
# Check out which keys are in europe by calling the keys() method on europe. Print out the result.
# Print out the value that belongs to the key 'norway'.

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print out the keys in europe
print(europe.keys())

# Print out value that belongs to key 'norway'
print(europe["norway"])



### Dictionary Manipulation (1)
# Instructions
# Add the key 'italy' with the value 'rome' to europe.
# To assert that 'italy' is now a key in europe, print out 'italy' in europe.
# Add another key:value pair to europe: 'poland' is the key, 'warsaw' is the corresponding value.
# Print out europe.

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add italy to europe
europe["italy"] = "rome"

# Print out italy in europe
print("italy" in europe)

# Add poland to europe
europe["poland"] = "warsaw"

# Print europe
print(europe)


### Dictionary Manipulation (2)
# Instructions
# The capital of Germany is not 'bonn'; it's 'berlin'. Update its value.
# Australia is not in Europe, Austria is! Remove the key 'australia' from europe.
# Print out europe to see if your cleaning work paid off.

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# Update capital of germany
europe["germany"] = "berlin"

# Remove australia
del(europe["australia"])

# Print europe
print(europe)


### Dictionariception
# Instructions
# Use chained square brackets to select and print out the capital of France.
# Create a dictionary, named data, with the keys 'capital' and 'population'. Set them to 'rome' and 59.83, respectively.
# Add a new key-value pair to europe; the key is 'italy' and the value is data, the dictionary you just built.

# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe["france"]["capital"])

# Create sub-dictionary data
data = {'capital':'rome',
      'population':59.83}

# Add data to europe under key 'italy'
europe.update({'italy': {'capital':'rome',
      'population':59.83}})

# Print europe
print(europe)



### Dictionary to DataFrame (1)
# Instructions
# Import pandas as pd.
# Use the pre-defined lists to create a dictionary called my_dict. There should be three key value pairs:
# key 'country' and value names.
# key 'drives_right' and value dr.
# key 'cars_per_cap' and value cpc.
# Use pd.DataFrame() to turn your dict into a DataFrame called cars.
# Print out cars and see how beautiful it is.

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {
    'country': ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt'],
    'drives_right': [True, False, False, False, True, True, True],
    'cars_per_cap': [809, 731, 588, 18, 200, 70, 45]
}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)



### Dictionary to DataFrame (2)
# Instructions
# Hit Run Code to see that, indeed, the row labels are not correctly set.
# Specify the row labels by setting cars.index equal to row_labels.
# Print out cars again and check if the row labels are correct this time.

import pandas as pd

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)


### CSV to DataFrame (1)
# Instructions
# To import CSV files you still need the pandas package: import it as pd.
# Use pd.read_csv() to import cars.csv data as a DataFrame. Store this DataFrame as cars.
# Print out cars. Does everything look OK?

# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv')

# Print out cars
print(cars)



### CSV to DataFrame (2)
# Instructions
# Run the code with Run Code and assert that the first column should actually be used as row labels.
# Specify the index_col argument inside pd.read_csv(): set it to 0, so that the first column is used as row labels.
# Has the printout of cars improved now?

# Import pandas as pd
import pandas as pd

# Fix import by including index_col
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out cars
print(cars)


### Square Brackets (1)
# Instructions
# Use single square brackets to print out the country column of cars as a Pandas Series.
# Use double square brackets to print out the country column of cars as a Pandas DataFrame.
# Use double square brackets to print out a DataFrame with both the country and drives_right columns of cars, in this order.

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
cars['country']

# Print out country column as Pandas DataFrame
print(cars['country'])

# Print out DataFrame with country and drives_right columns
print(cars[['country']])
print(cars[['country', 'drives_right']])

### Square Brackets (2)
# Instructions
# Select the first 3 observations from cars and print them out.
# Select the fourth, fifth and sixth observation, corresponding to row indexes 3, 4 and 5, and print them out.

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out first 3 observations
print(cars[0:3])

# Print out fourth, fifth and sixth observation
print(cars[3:6])


### loc and iloc (1)
# Instructions
# Use loc or iloc to select the observation corresponding to Japan as a Series. The label of this row is JPN, the index is 2. Make sure to print the resulting Series.
# Use loc or iloc to select the observations for Australia and Egypt as a DataFrame. You can find out about the labels/indexes of these rows by inspecting cars in the IPython Shell. Make sure to print the resulting DataFrame.

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out observation for Japan
print(cars.loc['JPN'])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS','EG']])


### loc and iloc (2)
# Instructions
# Print out the drives_right value of the row corresponding to Morocco (its row label is MOR)
# Print out a sub-DataFrame, containing the observations for Russia and Morocco and the columns country and drives_right.

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right value of Morocco
print(cars.loc['MOR', 'drives_right'])

# Print sub-DataFrame
print(cars.iloc[[4,5], [1,2]])



### loc and iloc (3)
# Instructions
# Print out the drives_right column as a Series using loc or iloc.
# Print out the drives_right column as a DataFrame using loc or iloc.
# Print out both the cars_per_cap and drives_right column as a DataFrame using loc or iloc.

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right column as Series
print(cars.loc[:, 'drives_right'])

# Print out drives_right column as DataFrame
print(cars.loc[:, ['drives_right']])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:, ['cars_per_cap', 'drives_right']])

