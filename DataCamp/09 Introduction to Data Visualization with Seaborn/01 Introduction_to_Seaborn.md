#### Introduction to Data Visualization with Seaborn

### Course Description

Seaborn is a powerful Python library that makes it easy to create informative and attractive data visualizations. This 4-hour course provides an introduction to how you can use Seaborn to create a variety of plots, including scatter plots, count plots, bar plots, and box plots, and how you can customize your visualizations.

You’ll explore this library and create Seaborn plots based on a variety of real-world data sets, including exploring how air pollution in a city changes through the day and looking at what young people like to do in their free time. This data will give you the opportunity to find out about Seaborn’s advantages first hand, including how you can easily create subplots in a single figure and how to automatically calculate confidence intervals.

By the end of this course, you’ll be able to use Seaborn in various situations to explore your data and effectively communicate the results of your data analysis to others. These skills are highly sought-after for data analysts, data scientists, and any other job that may involve creating data visualizations. If you’d like to continue your learning, this course is part of several tracks, including the Data Visualization track, where you can add more libraries and techniques to your skillset.

### Introduction to Seaborn

What is Seaborn, and when should you use it? In this chapter, you will find out! Plus, you will learn how to create scatter plots and count plots with both lists of data and pandas DataFrames. You will also be introduced to one of the big advantages of using Seaborn - the ability to easily add a third variable to your plots by using color to represent different subgroups.

## Making a scatter plot with lists

In this exercise, we'll use a dataset that contains information about 227 countries. This dataset has lots of interesting information on each country, such as the country's birth rates, death rates, and its gross domestic product (GDP). GDP is the value of all the goods and services produced in a year, expressed as dollars per person.

We've created three lists of data from this dataset to get you started. gdp is a list that contains the value of GDP per country, expressed as dollars per person. phones is a list of the number of mobile phones per 1,000 people in that country. Finally, percent_literate is a list that contains the percent of each country's population that can read and write.

- Import Matplotlib and Seaborn using the standard naming convention.

```
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
```

- Create a scatter plot of GDP (gdp) vs. number of phones per 1000 people (phones).

```
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create scatter plot with GDP on the x-axis and number of phones on the y-axis
sns.scatterplot(x=gdp, y=phones)
```

- Display the plot.

```
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create scatter plot with GDP on the x-axis and number of phones on the y-axis
sns.scatterplot(x=gdp, y=phones)

# Show plot
plt.show()
```

- Change the scatter plot so it displays the percent of the population that can read and write (percent_literate) on the y-axis.

```
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Change this scatter plot to have percent literate on the y-axis
sns.scatterplot(x=gdp, y=percent_literate)

# Show plot
plt.show()

```

## Making a count plot with a list

In the last exercise, we explored a dataset that contains information about 227 countries. Let's do more exploration of this data - specifically, how many countries are in each region of the world?

To do this, we'll need to use a count plot. Count plots take in a categorical list and return bars that represent the number of list entries per category. You can create one here using a list of regions for each country, which is a variable named region.

- Import Matplotlib and Seaborn using the standard naming conventions.
- Use Seaborn to create a count plot with region on the y-axis.
- Display the plot.

```
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns# Import Matplotlib and Seaborn


# Create count plot with region on the y-axis
sns.countplot(y=region)

# Show plot
plt.show()
```

## "Tidy" vs. "untidy" data

Here, we have a sample dataset from a survey of children about their favorite animals. But can we use this dataset as-is with Seaborn? Let's use pandas to import the csv file with the data collected from the survey and determine whether it is tidy, which is essential to having it work well with Seaborn.

To get you started, the filepath to the csv file has been assigned to the variable csv_filepath.

Note that because csv_filepath is a Python variable, you will not need to put quotation marks around it when you read the csv.

- Read the csv file located at csv_filepath into a DataFrame named df.
- Print the head of df to show the first five rows.

```
# Import pandas
import pandas as pd

# Create a DataFrame from csv file
df = pd.read_csv(csv_filepath)

# Print the head of df
print(df.head())
```

## Making a count plot with a DataFrame

In this exercise, we'll look at the responses to a survey sent out to young people. Our primary question here is: how many young people surveyed report being scared of spiders? Survey participants were asked to agree or disagree with the statement "I am afraid of spiders". Responses vary from 1 to 5, where 1 is "Strongly disagree" and 5 is "Strongly agree".

To get you started, the filepath to the csv file with the survey data has been assigned to the variable csv_filepath.

Note that because csv_filepath is a Python variable, you will not need to put quotation marks around it when you read the csv.

-  Matplotlib, pandas, and Seaborn using the standard names.
- Create a DataFrame named df from the csv file located at csv_filepath.
- Use the countplot() function with the x= and data= arguments to create a count plot with the "Spiders" column values on the x-axis.
- Display the plot.

```
# Import Matplotlib, pandas, and Seaborn
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Create a DataFrame from csv file
df = pd.read_csv(csv_filepath)

# Create a count plot with "Spiders" on the x-axis
sns.countplot(x="Spiders", data=df)

# Display the plot
plt.show()
```

## Hue and scatter plots

In the prior video, we learned how hue allows us to easily make subgroups within Seaborn plots. Let's try it out by exploring data from students in secondary school. We have a lot of information about each student like their age, where they live, their study habits and their extracurricular activities.

For now, we'll look at the relationship between the number of absences they have in school and their final grade in the course, segmented by where the student lives (rural vs. urban area).

- Create a scatter plot with "absences" on the x-axis and final grade ("G3") on the y-axis using the DataFrame student_data. Color the plot points based on "location" (urban vs. rural).

```
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a scatter plot of absences vs. final grade
sns.scatterplot(x="absences", y="G3", 
                data=student_data, 
                hue="location")

# Show plot
plt.show()
```

- Make "Rural" appear before "Urban" in the plot legend.

```
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Change the legend order in the scatter plot
sns.scatterplot(x="absences", y="G3", 
                data=student_data, 
                hue="location",
                hue_order=["Rural", "Urban"])

# Show plot
plt.show()
```

## Hue and count plots

Let's continue exploring our dataset from students in secondary school by looking at a new variable. The "school" column indicates the initials of which school the student attended - either "GP" or "MS".

In the last exercise, we created a scatter plot where the plot points were colored based on whether the student lived in an urban or rural area. How many students live in urban vs. rural areas, and does this vary based on what school the student attends? Let's make a count plot with subgroups to find out.

- Fill in the palette_colors dictionary to map the "Rural" location value to the color "green" and the "Urban" location value to the color "blue".
- Create a count plot with "school" on the x-axis using the student_data DataFrame.
- Add subgroups to the plot using "location" variable and use the palette_colors dictionary to make the location subgroups green and blue.

```
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a dictionary mapping subgroup values to colors
palette_colors = {"Rural": "green", "Urban": "blue"}

# Create a count plot of school with location subgroups
sns.countplot(x="school", data=student_data,
              hue="location",
              palette=palette_colors)

# Display plot
plt.show()
```