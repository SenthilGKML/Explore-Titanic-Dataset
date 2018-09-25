
# coding: utf-8

# In[3]:


import pandas as pd
train = pd.read_csv("/Users/GSENTH13/Desktop/studies/MachineLearning/all/train.csv", index_col="PassengerId")
test = pd.read_csv("/Users/GSENTH13/Desktop/studies/MachineLearning/all/test.csv", index_col="PassengerId")
train.shape


# In[5]:


train.head()


# In[7]:


test.shape


# In[9]:


test.head()


# In[10]:


get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(data=train, x="Sex", hue="Survived")


# In[11]:


pd.pivot_table(train, index="Sex", values="Survived")

