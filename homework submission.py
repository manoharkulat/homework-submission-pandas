#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


tf=pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv')
tf


# In[6]:


tf.dtypes['item_price']


# In[ ]:


#1) To insert total column which is product of values of quantity col and item_price col


# In[7]:


#removing $ sign and converting dtype of item_price col to float.
tf['item_price']=tf['item_price'].str.replace('$','')
tf['item_price']=tf['item_price'].astype(float)
tf.dtypes['item_price']


# In[8]:


#inserting total col 
tf['total']=tf['quantity']*tf['item_price']
tf


# In[11]:


#delete all rows with NaN values.
tf.dropna()


# In[12]:


#data2
tf2=pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/beer.txt',sep=' ')
tf2


# In[13]:


#finding max and min values of cost column
tf2[tf2['cost']==max(tf2['cost'])]


# In[14]:


tf2[tf2['cost']==min(tf2['cost'])].cost


# In[15]:


#increase alcohol by 2 unit each
tf2['alcohol']=tf2['alcohol']+2
tf2


# In[16]:


#filter sodium unit between 4 to 5 and corresponding name
rang=tf2['sodium'].between(15,20 , inclusive=True)
tf2[rang][['name']]


# In[17]:


#other filters
tf2.filter(items=['calories', 'cost'])


# In[18]:


tf2.filter(regex='1$', axis=0) 


# In[19]:


#apply operation on perticular column using agg method.
tf2['calories'].aggregate("mean")


# In[20]:


#along the row all results
tf2.agg(['sum','min'])


# In[21]:


#permutation & combination
for i in tf2['cost']:
    if i >0.4:
        print(i)


# In[22]:


tf2['cost'][0:3]


# In[23]:


#applying append function of list
for i in range(5):
    tf2=tf2.append({'cost':i},ignore_index=True)
tf2


# In[24]:


#sorting
tf2.sort_values(by=['calories'])


# In[26]:


#inserting
#inserting new column
tf2.insert(4,"total",[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25])
tf2


# In[ ]:




