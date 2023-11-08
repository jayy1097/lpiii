#!/usr/bin/env python
# coding: utf-8

# In[25]:


import numpy as np
import matplotlib.pyplot as plt


# In[33]:


x = 2
rate = 0.01
precision = 0.000001
step = 1
iteration = 1000
iter = 1
gdf = lambda x:(x+3)**2
arr = []


# In[34]:


def slope(x):
    return 2*(x+3)
def eq(x):
    return (x+3)**2


# In[35]:


while iteration > iter and step > precision:
    prev = x
    x = x - rate*slope(x)
    step = abs(x-prev)
    arr.append(x)
    iter+=1
    print(f"Iteration {iter} : {x}")


# In[37]:


print(f"Local Minima : {x}")


# In[46]:


line = np.linspace(-5,5,100)
arr = np.array(arr)
plt.plot(line,eq(line))
plt.plot(arr,eq(arr) , color='red')


# In[ ]:




