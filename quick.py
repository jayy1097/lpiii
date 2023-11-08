#!/usr/bin/env python
# coding: utf-8

# In[35]:


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x==pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)


# In[36]:


import random
N = int(input("Enter no. of terms : "))
arr = [random.randint(1,100) for _ in range(N)]
print(arr)
arr = quicksort(arr)
print(arr)


# In[ ]:





# In[ ]:




