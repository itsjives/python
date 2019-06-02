
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

income = np.random.normal(100.0, 20.0, 10000)

plt.hist(income, 50)
plt.show(50)


# In[3]:


income.std()


# In[4]:


income.var()

