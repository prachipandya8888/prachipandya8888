#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd 
import numpy as np
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm','Budapest_PaRis', 'Brussels_londOn'],
                   'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
                   'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
                   'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )','12. Air France', '"Swiss Air"']})


# SOLUTION:
# 

# In[4]:


# load pandas and numpy module

import pandas as pd 
import numpy as np


# In[5]:


#solution

#load dataset

df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm','Budapest_PaRis', 'Brussels_londOn'],
                   'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
                   'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
                   'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )','12. Air France', '"Swiss Air"']})
df_Analysis = df

print("dataset")

df_Analysis


# 1 . Some values in the the FlightNumber column are missing. These numbers are meant to increase by 10 with each row so 10055 and 10075 need to be put in place. Fill in these missing numbers and make the column an integer column (instead of a float column).

# In[6]:


# to prevent jupyter warning action
pd.options.mode.chained_assignment = None


x,y = df_Analysis.FlightNumber.loc[[0]].values[0]+10, df_Analysis.FlightNumber.loc[[4]].values[0]-10

df_Analysis.FlightNumber.loc[[1]]=df_Analysis.FlightNumber.loc[[1]].fillna(x)

df_Analysis.FlightNumber.loc[[3]]=df_Analysis.FlightNumber.loc[[3]].fillna(y)

# convert flot type to int type
df_Analysis.FlightNumber = df_Analysis.FlightNumber.astype(int)

print("Output")
df_Analysis


# 2. The FromTo column would be better as two separate columns! Split each string on the underscore delimiter to give a new temporary DataFrame with the correct values. Assign the correct column names to this temporary DataFrame.

# In[7]:


df_temp=df_Analysis.From_To.str.split('_', expand=True)
df_temp.columns = ['From','To']
print("output")
df_temp


# 3 . Notice how the capitalisation of the city names is all mixed up in this temporary DataFrame. Standardise the strings so that only the first letter is uppercase (e.g. "londON" should become "London".)

# In[8]:


df_temp.From = df_temp.From.str.title()
df_temp.To = df_temp.To.str.title()
print("output")
df_temp


# 4 . Delete the From_To column from df and attach the temporary DataFrame from the previous questions.

# In[12]:


df_Analysis=df_Analysis.drop("From_To", axis=1).join(df_temp)
print("Output")
df_Analysis


# 5 . In the RecentDelays column, the values have been entered into the DataFrame as a list. We would like each first value in its own column, each second value in its own column, and so on. If there isn't an Nth value, the value should be NaN.
# 
# Expand the Series of lists into a DataFrame named delays, rename the columns delay_1, delay_2, etc. and replace the unwanted RecentDelays column in df with delays.
# 
# 

# In[10]:


df_delays=pd.DataFrame(df_Analysis["RecentDelays"].values.tolist())
df_delays.columns = ['delay_{}'.format(n) for n in range(1, len(df_delays.columns)+1)]
df_delays


# In[11]:


df_Analysis=df_Analysis.drop("RecentDelays" , axis=1).join(df_delays)
print("Output")
df_Analysis

