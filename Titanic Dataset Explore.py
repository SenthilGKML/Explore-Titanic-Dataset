
# coding: utf-8

# Importing the train and test csv Dataset

import pandas as pd
train = pd.read_csv("/MachineLearning/all/train.csv", index_col="PassengerId")
test = pd.read_csv("/MachineLearning/all/test.csv", index_col="PassengerId")
train.shape


# Verifying the train Dataset using head() method

train.head()


# Verifying the test Dataset using head() method

test.shape

test.head()


# Check the output in Seaborn 


get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(data=train, x="Sex", hue="Survived")


# Check the output in Pivot Table


pd.pivot_table(train, index="Sex", values="Survived")

