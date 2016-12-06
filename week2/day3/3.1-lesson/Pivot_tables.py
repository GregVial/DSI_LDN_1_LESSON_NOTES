
# coding: utf-8

# In[9]:

import pandas as pd
import numpy as np


# Load data set (excel)

# In[10]:

sales_funnel_df = pd.read_excel("sales-funnel.xlsx")
sales_funnel_df.head()


# In[11]:

sales_funnel_df['Status'] = sales_funnel_df['Status'].astype("category")
sales_funnel_df['Account'] = sales_funnel_df['Account'].astype('category')


# In[12]:

pd.pivot_table(sales_funnel_df, index=["Name"])


# In[13]:

pd.pivot_table(sales_funnel_df, index=["Name", 'Rep', 'Manager'])


# In[14]:

pd.pivot_table(sales_funnel_df, index=["Manager", "Rep", "Name"])


# We can drop the account name from the index

# In[15]:

pd.pivot_table(sales_funnel_df, index=["Manager", "Rep"])


# We can also specify the columns to be aggregated. For ex: price

# In[16]:

pd.pivot_table(sales_funnel_df, index=["Manager", "Rep"], values=['Price'])


# We can change the aggregation strategy. For ex: to get the sum of values instead of the mean.

# In[18]:

pd.pivot_table(sales_funnel_df, index=['Manager', 'Rep'], values=['Price'],
              aggfunc=sum)


# In[19]:

pd.pivot_table(sales_funnel_df, index=['Manager', 'Rep'], values=['Price'],
              aggfunc=[sum, len])


# In[23]:

pd.pivot_table(sales_funnel_df, index=['Manager', 'Rep'], 
               columns=['Product'],
               values=['Price'], aggfunc=[np.sum])


# In[24]:

pd.pivot_table(sales_funnel_df, index=['Manager', 'Rep'], 
               columns=['Product'], values=['Price'], 
               aggfunc=[np.sum], fill_value=0)


# In[25]:

pd.pivot_table(sales_funnel_df, index=['Manager', 'Rep', 'Product'], 
               values=['Price'], 
               aggfunc=[np.sum], fill_value=0)


# In[26]:

pd.pivot_table(sales_funnel_df, index=['Manager', 'Rep', 'Product'],
                values=['Price'], aggfunc=[np.sum, len], fill_value=0,
              margins=True)


# In[29]:

pd.pivot_table(sales_funnel_df, index=["Status"], columns=["Manager"],
              values=['Price'], aggfunc=[np.sum, len], margins=True)


# In[32]:

table = pd.pivot_table(sales_funnel_df, index=['Manager', 'Status'],
                      columns=['Product'], values=['Quantity', 'Price'],
                      aggfunc={'Quantity': len, 'Price': [np.sum, len]},
                      fill_value=0)
table


# In[33]:

table.query('Manager == ["Debra Henley"]')


# In[34]:

table.query("Status != ['won']")


# In[36]:

table['Quantity'].query("Status != ['won']")


# In[ ]:



