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

    > - Import Matplotlib and Seaborn using the standard naming convention.
    > - Create a scatter plot of GDP (gdp) vs. number of phones per 1000 people (phones).
    > - Display the plot.
    > - Change the scatter plot so it displays the percent of the population that can read and write (percent_literate) on the y-axis.

```
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns


# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create scatter plot with GDP on the x-axis and number of phones on the y-axis
sns.scatterplot(x=gdp, y=phones)


# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create scatter plot with GDP on the x-axis and number of phones on the y-axis
sns.scatterplot(x=gdp, y=phones)

# Show plot
plt.show()


# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Change this scatter plot to have percent literate on the y-axis
sns.scatterplot(x=gdp, y=percent_literate)

# Show plot
plt.show()

```
