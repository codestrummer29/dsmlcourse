#!/usr/bin/env python
# coding: utf-8

import numpy as np


# #### Create an array of 10 zeros 

# In[7]:


np.zeros(10)


# #### Create an array of 10 ones

# In[8]:


np.ones(10)


# #### Create an array of 10 fives

# In[9]:


np.ones(10)*5


# #### Create an array of the integers from 10 to 50

# In[10]:


np.arange(10,51)


# #### Create an array of all the even integers from 10 to 50

# In[11]:


np.arange(10,51,2)


# #### Create a 3x3 matrix with values ranging from 0 to 8

# In[12]:


np.arange(9).reshape(3,3)


# #### Create a 3x3 identity matrix

# In[13]:


np.eye(3)


# #### Use NumPy to generate a random number between 0 and 1

# In[8]:


np.random.rand(1)


# #### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

# In[54]:


np.random.randn(25)


# #### Create the following matrix:

# In[33]:


arr = np.arange(1,101)/100
arr.reshape(10,10)


# #### Create an array of 20 linearly spaced points between 0 and 1:

# In[34]:


np.linspace(0,1,20)


# ## Numpy Indexing and Selection
# 
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

# In[36]:


mat = np.arange(1,26).reshape(5,5)
mat


# In[38]:


mat[2:,1:]


mat[3,4]


# In[41]:





# In[44]:


mat[:3,1:2]


# In[42]:





# In[56]:


mat[4]


# In[46]:





# In[46]:


mat[3:,:]


# In[49]:





# ### Now do the following

# #### Get the sum of all the values in mat

# In[48]:


mat.sum()


# #### Get the standard deviation of the values in mat

# In[52]:


mat.std()


# #### Get the sum of all the columns in mat

# In[59]:


mat.sum(0)


# # Great Job!
