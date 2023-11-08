#!/usr/bin/env python
# coding: utf-8

# In[67]:


keys = ['E','N','G','I','R']
items = [3,3,2,2,1]
keys2 = list(keys)
encode = []
graph = {}


# In[68]:


def Huff(keys,items):
    while len(items) > 1:
        data = list(zip(items,keys))
        data.sort(key=lambda x:x[0])
        items,keys = zip(*data)
        new = items[0] + items[1]
        graph[new] = [keys[0],keys[1]]
        items = list(items[2:])
        keys = list(keys[2:])
        items.append(new)
        keys.append(new)
    return new


# In[69]:


def dfs(visited,graph,node,bit):
    if node in keys2:
        visited.append(bit)
        print(f"Encoding for {node} is : {visited[1:]}")
    else:
        visited.append(bit)
        if node in graph:
            bit=1
            for neighbour in graph[node]:
                if bit==1:
                    bit=0
                else:
                    bit=1
                dfs(visited.copy(),graph,neighbour,bit)


# In[70]:


root = Huff(keys,items)
dfs(encode,graph,root,1)


# In[ ]:




