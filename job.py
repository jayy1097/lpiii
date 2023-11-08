#!/usr/bin/env python
# coding: utf-8

# In[77]:





# In[106]:


def job_sc(arr,t):
    size = len(arr)
    for i in range(size-1):
        for j in range(size-1-i):
            if arr[j][2] < arr[j+1][2]:
                (arr[j],arr[j+1]) = (arr[j+1],arr[j])
    jobs = [-1]*t
    for i in range(size):
        for j in range(min(t-1,arr[i][1]-1),-1,-1):
            if jobs[j] == -1:
                jobs[j]=arr[i][0]
                break
    print(jobs)
arr = [['a',2,100],
      ['b',3,15],
      ['c',1,20],
      ['d',2,27],
      ['e',1,10]]
x = 0
for i in range(len(arr)):
    if x < arr[i][1]:
        x = arr[i][1]
job_sc(arr,x)


# In[ ]:




