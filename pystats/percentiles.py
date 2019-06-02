
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

vals = np.random.normal(0, 0.5, 10000)

plt.hist(vals, 50)
plt.show()


# In[3]:


#percentile another name for median
np.percentile(vals, 50)


# In[4]:


np.percentile(vals, 90)


# In[5]:


np.percentile(vals, 20)

