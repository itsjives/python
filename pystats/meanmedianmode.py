
# coding: utf-8

# In[1]:


import numpy as np
incomes = np.random.normal(270000, 15000, 10000)
np.mean(incomes)


# In[4]:


import matplotlib.pyplot as plt
plt.hist(incomes, 50)
plt.show()


# In[5]:


np.median(incomes)


# In[6]:


incomes = np.append(incomes, [1000000000])


# In[7]:


np.median(incomes)


# In[8]:


np.mean(incomes)


# In[15]:


ages = np.random.randint(18, high=90, size=500)
ages


# In[16]:


from scipy import stats
stats.mode(ages)


# In[22]:


import numpy as np
import matplotlib.pyplot as plt

income = np.random.normal(100.0, 20.0, 10000)

plt.hist(incomes, 50)
plt.show()


# In[23]:


np.mean(income)


# In[24]:


np.median(income)

