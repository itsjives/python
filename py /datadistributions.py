
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

values = np.random.uniform(-10.0, 10.0, 100000)

plt.hist(values, 50)
plt.show()


# In[3]:


from scipy.stats import norm
import matplotlib.pyplot as plt

x = np.arange(-3, 3, 0.001)
plt.plot(x, norm.pdf(x))


# In[4]:


import numpy as np
import matplotlib.pyplot as plt

mu = 5.0
sigma = 2.0 
values = np.random.normal(mu, sigma, 10000)
plt.hist(values, 50)
plt.show()


# In[6]:


from scipy.stats import expon 
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.001)
plt.plot(x, expon.pdf(x))


# In[8]:


#Binomial Probability mass function

from scipy.stats import binom 
import matplotlib.pyplot as plt

n, p = 10, 0.5 
x = np.arange(0, 10, 0.001)
plt.plot(x, binom.pmf(x, n, p))


# In[9]:


#Poisson Probability mass function 

from scipy.stats import poisson 
import matplotlib.pyplot as plt

#mu is average

mu = 500
x = np.arange(400, 600, 0.5)
plt.plot(x, poisson.pmf(x, mu))

