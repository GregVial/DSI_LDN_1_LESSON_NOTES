
# coding: utf-8

# In[1]:

import pandas as pd


# ### Categorical variables

# In[2]:

# Let's use pandas to create Categorical Series. One way is by 
# specifying dtype="category" when constructing a Series:

s = pd.Series(["a","b","c","a"], dtype="category")
s


# In[3]:

# Another way is to convert an existing Series or column to a 
# category dtype:

df = pd.DataFrame({"A":["a","b","c","a"]})
df["B"] = df["A"].astype('category')
df


# In[4]:

df.dtypes


# In[5]:

# You can also pass a pandas.Categorical object to a Series 

raw_cat = pd.Categorical(["a","b","c","a"], categories=["b","c","d"],
                          ordered=False)


# In[6]:

s = pd.Series(raw_cat)
s


# ### Dummy variables

# In[12]:

# Let's use pd.get_dummies to convert categorical variables into dummy 
# variables. First let's create a small DataFrame with categorical variables. 

df = pd.DataFrame({'key': list('bbacab'), 'data1': range(6)})
df


# In[11]:

# Now, let's convert the categorical variables into dummy variables. 

pd.get_dummies(df['key'])


# In[14]:

df[['dummy_a', 'dummy_b', 'dummy_c']] = pd.get_dummies(df['key'])


# In[15]:

df


# In[ ]:



