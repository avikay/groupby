#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[11]:


#lets create a dictionary to further create a dataframe
d ={'company': ['Neo','Neo','Orac','Orac','Nero','Nero'],
    'person': ['Sam','Ana','Avi','Varun','Pat','Ash'],
    'sales':[2000,5000,9999999999,10000,10,10000000]}


# In[12]:


df = pd.DataFrame(d)


# In[13]:


df


# In[7]:


#as in sql groupby is used to create some aggregate values out of certain parameters here the companies
agg = df.groupby('company')


# In[14]:


#we've now created an object that have the values of companies 
agg


# ##### some aggregate methods with groupby

# In[15]:


#trying some function and checking wether the created object is working fine
#mean of sales based on companies
agg.mean()


# In[17]:


#sum of sales
agg.sum()


# In[18]:


#standard deviation of sales
agg.std()


# In[19]:


#fetching any particular data after applying a funtion on the groupby object
agg.mean().loc['Orac']


# In[20]:


#doing the same process without storing it in a variable or an object:
#getting rows
df.groupby('company').sum()['sales']


# In[22]:


#getting columns
df.groupby('company').std().loc['Nero']


# In[23]:


#count the number of instances under each company
df.groupby('company').count()


# In[25]:


#it will return the maximum of sales under each company
#but it will also return strings on the basis of higher index of alphabets or alphabets at the last of A-Z
df.groupby('company').max()


# In[27]:


#it will return strings that are at the begining of A-Z
df.groupby('company').min()


# In[29]:


#it will provide some values with multiple functions at once
df.groupby('company').describe()


# In[30]:


#we can transpose the desccribe table as:
df.groupby('company').describe().transpose()


# In[31]:


df.groupby('company').describe().transpose()['Nero']


# In[ ]:




