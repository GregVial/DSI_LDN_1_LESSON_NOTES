
# coding: utf-8

# # Local Postgresql Database Lab
# 
# In this lab we will practice adding and removing data from a local Postgresql database. We will:
# 
# - Walk through instructions on how to set up and configure a local postgresql server
# - Create a database and a table using SQL and CRUD data in/from that table.
# - Learn how to copy data from a CSV file into this local database
# - Practice our SQL with a practice assignment.

# ## 1. Install PostgreSQL Locally
# 
# You should have already taken care of this in the Installfest, but just in case, [here](http://www.postgresql.org/download/) are the instructions for the most common platforms.

# ## 2. Launch and connect to a local PostgreSQL server
# 
# Now that you've installed PostgreSQL locally, practice connecting with the following methods:
# 
# - [Postico](https://eggerapps.at/postico/docs/v1.0.6/)
# - Command-line (psql)
# - Sqlalchemy + Pandas
# - Ipython-notebook using the ipython-sql extension
# 
# **Check:** List the existing databases, there should be none, right?
# > not true, there are some default databases from postgres
# 
# **Check:** If there are databases, check the tables' contents.

# In[1]:

#- from sqlalchemy
from sqlalchemy import create_engine
import pandas as pd
engine = create_engine('postgresql://localhost:5432')
pd.read_sql("SELECT * FROM information_schema.tables LIMIT 3;", engine)


# In[2]:

# - the ipython-notebook using the ipython-sql extension
get_ipython().magic(u'load_ext sql')


# In[3]:

get_ipython().run_cell_magic(u'sql', u'postgresql://localhost:5432', u'\nSELECT * FROM information_schema.tables LIMIT 3;')


# ## 3. Create DB
# Once you are connected to your local Postgresql server, create a new database. Call it `lab33`.
# 
# Practice creating and deleting the database with the following methods:
# 
# - Postico
# - Command-line:
# >     create database lab33
# >     drop database lab33
# 
# - Sqlalchemy
# - Ipython-notebook using the ipython-sql extension
# 
# **Check:** If you create a DB in Postico, do you see it from the command-line?
# > Yes
# 
# **Check:** What does this tell us about multiple connections to the same db?
# > Multiple users/connections are possible and the data is consistent. Postgres is relational -> ACID.

# In[9]:

# sqlalchemy
conn = engine.connect()
conn.execute("commit")
conn.execute("create database lab33")
conn.close()


# In[8]:

get_ipython().run_cell_magic(u'sql', u'', u'create database lab33\n# drop database lab33')


# ## 4. CRUD (Create, Read, Update, and Delete)
# 
# In lesson 1.1 you learned how to add and remove data from sqlite. Let's review that on our local PostgreSQL installation.

# ### 4.a: Creating Tables and Adding Columns
# 
# 1. Create an table called `table1` with a single column `field1` containing an INTEGER PRIMARY KEY. Practice doing this with any of the methods above.
# - Add a few more columns to `table1`:
#     - field2 VARCHAR(16)
#     - field3 REAL
#     - field4 TEXT
# check [the doc](http://www.postgresql.org/docs/9.3/static/datatype.html) for more info on data types supported by postgresql.
# - Check tables and schemas using command line or postico

# In[10]:

get_ipython().run_cell_magic(u'sql', u'postgresql://localhost:5432/lab33', u'\nCREATE TABLE table1 (field1 INTEGER PRIMARY KEY);')


# In[11]:

get_ipython().run_cell_magic(u'sql', u'', u'ALTER TABLE table1 ADD COLUMN field2 VARCHAR(16);\nALTER TABLE table1 ADD COLUMN field3 REAL;\nALTER TABLE table1 ADD COLUMN field4 TEXT;')


# ### 4.b: Add Data
# 
# Add some data to `table1`:
# 
# |field1|field2|field3|field4|
# |----|
# |1|'Henry James'|42|'75 Mission Street, San Francisco, CA'|
# |2|'Carol James'|40|'75 Mission Street, San Francisco, CA'|
# |3|'Jesse James'|12|'75 Mission Street, San Francisco, CA'|

# In[12]:

get_ipython().run_cell_magic(u'sql', u'', u"INSERT INTO table1 VALUES (1, 'Henry James', 42, '75 Mission Street, San Francisco, CA');\nINSERT INTO table1 VALUES (2, 'Carol James', 40, '75 Mission Street, San Francisco, CA');\nINSERT INTO table1 VALUES (3, 'Jesse James', 12, '75 Mission Street, San Francisco, CA');")


# ### 4.c: Read Data
# Read the content of the table,

# In[13]:

get_ipython().run_cell_magic(u'sql', u'', u'select * from table1;')


# ### 4.d: Update Records
# Suppose we need to update an existing record with new data - e.g. maybe `Jesse James` is only 9. Use the update command to do this.

# In[14]:

get_ipython().run_cell_magic(u'sql', u'', u'UPDATE table1 SET field3=9 WHERE field1=3;\nselect * from table1;')


# ### 4.e: Remove Records
# To remove records use the DELETE command. Delete the entry for anyone matching `Jesse`.

# In[15]:

get_ipython().run_cell_magic(u'sql', u'', u"DELETE FROM table1 WHERE field2 like '%Jesse%';\nselect * from table1;")


# ## 5. Data from CSV
# 
# Copy CSV data from a local file into a local PostgreSQL database. We will use a [dataset](../../assets/datasets/Eviction_Notices.csv) pulled from the SF open data website. It contains a set of eviction notices issued in San Francisco.
# 
# Open the data in a text editor and have a look at it.

# ### 5.a: Simple Import
# 
# Read [this post](http://stackoverflow.com/questions/2987433/how-to-import-csv-file-data-into-a-postgresql-table) to learn how you can import data from CSV to PostgreSQL.
# 
# Notice that you have to decide the type for each column. Let's keep it simple and import everything as a string of text for now.
# 
# - Create a table called `evictions_simple` and import the data as varchar.
# - Check that everything worked fine by loading a few lines from the table.
# - Try some simple queries:
#     - count how many evictions are due to non_payments
#     - list the 3 most recent evictions
# 
# 
# **Hint:** A good practice when you create a new table is to always drop it first, in case it already exists.
# 
# **Check:** Did you avoid importing the header as a record?

# In[29]:

get_ipython().run_cell_magic(u'sql', u'', u"DROP TABLE IF EXISTS evictions_simple;\nCREATE TABLE evictions_simple\n(eviction_id varchar,\n address varchar,\n city varchar,\n state varchar,\n zip varchar,\n file_date varchar,\n non_payment varchar,\n breach varchar,\n nuisance varchar,\n illegal_use varchar,\n failure_to_sign_renewal varchar,\n access_denial varchar,\n unapproved_subtenant varchar,\n owner_move_in varchar,\n demolition varchar,\n capital_improvement varchar,\n substantial_rehab varchar,\n ellis_act_withdrawal varchar,\n condo_conversion varchar,\n roommate_same_unit varchar,\n other_cause varchar,\n late_payments varchar,\n lead_remediation varchar,\n development varchar,\n good_samaritan_ends varchar,\n constraints varchar,\n constraints_date varchar,\n supervisor_district varchar,\n neighborhood varchar,\n client_location varchar);\n\n\nCOPY evictions_simple FROM '/Users/juan/project/general_assembly/DSI-course-materials/curriculum/04-lessons/week-05/3.3-lab/assets/datasets/Eviction_Notices.csv' DELIMITER ',' CSV HEADER;")


# In[30]:

import os
os.getcwd()


# In[31]:

get_ipython().run_cell_magic(u'sql', u'', u'select * from evictions_simple limit 3;')


# In[32]:

get_ipython().run_cell_magic(u'sql', u'', u"select count(*) from evictions_simple\nwhere non_payment = 'true';")


# In[33]:

get_ipython().run_cell_magic(u'sql', u'', u'select * from evictions_simple\norder by file_date desc\nlimit 3;')


# ### 5.b: Data Cleaning and Import
# 
# If you've executed the last query correctly (most recent evictions), you'll have noticed that the dates are not correctly understood. This is because we were sloppy and imported the data as string for all fields.
# 
# Let's see what data types we would ideally like to have for each column.
# 
# [Here are data types](http://www.tutorialspoint.com/postgresql/postgresql_data_types.htm)
# 
# - Discuss in pairs each column and then let's summarize together. Which data type would you choose for each field?
# - Repeat the import to a new table called `evictions`. Notice that line 31494 may throw an error. Why is that?
# > There are two ` characters that do not belong.
# - Repeat the query for the 3 most recent evictions. Does it work now?

# In[35]:

get_ipython().run_cell_magic(u'sql', u'', u'SET DATESTYLE TO "ISO,MDY";')


# In[36]:

get_ipython().run_cell_magic(u'sql', u'', u"DROP TABLE IF EXISTS evictions;\nCREATE TABLE evictions\n(eviction_id varchar,\n address varchar,\n city varchar,\n state char(2),\n zip char(5),\n file_date date,\n non_payment boolean,\n breach boolean,\n nuisance boolean,\n illegal_use boolean,\n failure_to_sign_renewal boolean,\n access_denial boolean,\n unapproved_subtenant boolean,\n owner_move_in boolean,\n demolition boolean,\n capital_improvement boolean,\n substantial_rehab boolean,\n ellis_act_withdrawal boolean,\n condo_conversion boolean,\n roommate_same_unit boolean,\n other_cause boolean,\n late_payments boolean,\n lead_remediation boolean,\n development boolean,\n good_samaritan_ends boolean,\n constraints boolean,\n constraints_date date,\n supervisor_district integer,\n neighborhood varchar,\n client_location varchar);\n\n\nCOPY evictions FROM '/Users/juan/project/general_assembly/DSI-course-materials/curriculum/04-lessons/week-05/3.3-lab/assets/datasets/Eviction_Notices.csv' DELIMITER ',' CSV HEADER;")


# In[28]:

get_ipython().run_cell_magic(u'sql', u'', u'select * from evictions\norder by file_date desc\nlimit 3;')


# ## 6. Queries
# 
# Now that we have imported the data with correct data types, let's query the `evictions` table and find out a few things about SF and evictions.
# 
# Questions:
# - How many neighborhoods are there in SF? List them alphabetically
# - How many supervisor districts? 
# - How many unique zip codes?
#     - Are there any bad data in these? how many?
# - What are the top 5 causes of eviction?

# ### 6.a: How many neighborhoods are there in SF? List them alphabetically.

# In[58]:

get_ipython().run_cell_magic(u'sql', u'', u'select count(distinct neighborhood) from evictions;')


# In[59]:

get_ipython().run_cell_magic(u'sql', u'', u'select distinct neighborhood from evictions\norder by neighborhood;')


# ### 6.b: How many supervisor districts?

# In[61]:

get_ipython().run_cell_magic(u'sql', u'', u'select distinct supervisor_district from evictions\norder by supervisor_district;')


# ### 6.c how many unique zip codes?
# 
# Are there any bad data in these?

# In[64]:

get_ipython().run_cell_magic(u'sql', u'', u'select distinct zip from evictions\norder by zip;')


# ### 6.d: What are the top 5 causes of eviction?
# 
# You may find it easier to answer this question using pandas.

# In[75]:

engine = create_engine('postgresql://localhost:5432/lab33')
evictions = pd.read_sql("SELECT * FROM evictions;", engine)


# In[79]:

cause_list = ["non_payment",
              "breach",
              "nuisance",
              "illegal_use",
              "failure_to_sign_renewal",
              "access_denial",
              "unapproved_subtenant",
              "owner_move_in",
              "demolition",
              "capital_improvement",
              "substantial_rehab",
              "ellis_act_withdrawal",
              "condo_conversion",
              "roommate_same_unit",
              "other_cause",
              "late_payments",
              "lead_remediation",
              "development",
              "good_samaritan_ends"]


# In[84]:

evictions[cause_list].sum().sort_values(ascending = False)


# ## Bonus
# - Let's count the number of evictions for each year
#     - How has the number varied?
#     - Can you compare this with the nasdaq index? (use the DataReader module in Pandas to get the data)
# 

# In[85]:

evictions.info()


# In[111]:

get_ipython().run_cell_magic(u'sql', u'', u'select extract(year from file_date) as yyyy,\n       count(eviction_id) as evictions\nfrom evictions\ngroup by 1\norder by 1')


# In[112]:

evictions_by_year = _.DataFrame()


# In[118]:

evictions_by_year =evictions_by_year.set_index('yyyy')


# In[119]:

get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt


# In[125]:

evictions_by_year


# In[121]:

evictions_by_year.plot()


# In[122]:

from pandas.io.data import DataReader
import datetime


# In[129]:

nasdaq = DataReader("NASDAQ:NDAQ", "google", start=datetime.datetime(1990, 1, 1))


# In[130]:

nasdaq['Close'].plot()


# In[133]:

nasdaq_year_avg = nasdaq['Close'].groupby(pd.TimeGrouper('A')).mean()
nasdaq_year_avg


# In[139]:

nasdaq_year_avg.index = evictions_by_year.loc[2002:].index


# In[140]:

evictions_by_year['nasdaq'] = nasdaq_year_avg


# In[147]:

evictions_by_year['evictions'].plot()
evictions_by_year['nasdaq'].plot(secondary_y=True)

