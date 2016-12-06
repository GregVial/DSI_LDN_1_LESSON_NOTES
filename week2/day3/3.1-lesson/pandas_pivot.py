
# coding: utf-8

# In[2]:

import pandas as pd
import numpy as np


# We load the data set (excel)

# In[3]:

sales_funnel_df = pd.read_excel("sales-funnel.xlsx")
sales_funnel_df


# We change the type of Status and Account into Categories (categorical data)

# In[28]:

sales_funnel_df["Status"] = sales_funnel_df["Status"].astype("category")
sales_funnel_df["Account"] = sales_funnel_df["Account"].astype("category")


# We start with a simple pivot. Note that the aggregation function is the mean. Ex: for Kulas/Quantity, two rows [1, 2] => Quantity = 1.5

# In[30]:

pd.pivot_table(sales_funnel_df, index=["Name"])


# We now do a pivot using multiple columns for the Index

# In[31]:

pd.pivot_table(sales_funnel_df, index=['Name', 'Rep', 'Manager'])


# Please notice that if we change the order in the index, pandas detects the relations between managers and reps and groups them automatically.

# In[32]:

pd.pivot_table(sales_funnel_df, index=['Manager',  'Rep', 'Name'])


# Now, thinking only about understanding the sales funnel for each salesman, we drop the account name from the index

# In[34]:

pd.pivot_table(sales_funnel_df, index=['Manager', 'Rep'])


# We can also specify the columns to be aggregated. For ex: Price

# In[35]:

pd.pivot_table(sales_funnel_df, index=['Manager', 'Rep'], values=['Price'])


# So far for the aggregating columns we have been getting the mean value. We can specify another aggregation strategy with the aggfunc parameter

# In[36]:

pd.pivot_table(sales_funnel_df, index=["Manager", "Rep"], values=['Price'], aggfunc=np.sum)


# We can also give a list of functions to aggfunc, and it will get that agggregation for all the values

# In[37]:

pd.pivot_table(sales_funnel_df, index=["Manager", "Rep"], values=['Price'], aggfunc=[np.sum, len])


# We can also define columns to further segment our values. Remember that the aggregations are always done on the values.

# In[41]:

pd.pivot_table(sales_funnel_df, index=["Manager", "Rep"], values=['Price'], 
               columns=['Product'] ,aggfunc=[np.sum, len])


# You can notice that some values are NaN (more on this in the last lesson of the day).
# We can change those NaNs into zeros.

# In[42]:

pd.pivot_table(sales_funnel_df, index=["Manager", "Rep"], values=['Price'], 
               columns=['Product'] ,aggfunc=[np.sum, len], fill_value=0)


# If we move Products into the index, we have another way of summarizing the same info.

# In[44]:

pd.pivot_table(sales_funnel_df, index=["Manager", "Rep", "Product"], values=['Price'], 
               aggfunc=[np.sum, len], fill_value=0)


# We can also use margin, to get a total for each value column.

# In[45]:

pd.pivot_table(sales_funnel_df, index=["Manager", "Rep", "Product"], values=['Price'], 
               aggfunc=[np.sum, len], fill_value=0, margins=True)


# We can go up a level and try to analyse the value of the funnel for each manager, de aggregating on each status.

# In[48]:

pd.pivot_table(sales_funnel_df, index=["Manager", "Status"], values=['Price'], aggfunc=[np.sum, len])


# Another trick is to pass a dict for aggfun so we can specify different aggregation strategies for each value. Also, each value of the dict can be a list, as usual.

# In[52]:

table = pd.pivot_table(df,index=["Manager","Status"],columns=["Product"],values=["Quantity","Price"],
               aggfunc={"Quantity":len,"Price":[np.sum, len]},fill_value=0)
print table


# Finally, once we have a pivot we are happy with, we can also query it.

# In[53]:

table.query('Manager == ["Debra Henley"]')


# In[54]:

table.query("Status != ['won']")


# In[ ]:



