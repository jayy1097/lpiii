#!/usr/bin/env python
# coding: utf-8

# In[71]:





# In[83]:


class Item:
    def __init__(self,value,weight):
        self.value = value
        self.weight = weight

def Knapsack(W,arr):
    final_value=0
    arr.sort(key=lambda x:x.value/x.weight , reverse=True)
    for item in arr:
        if item.weight <= W:
            final_value+=item.value
            W-=item.weight
        else:
            final_value+=(W*item.value)/item.weight
            break
    return final_value


# In[84]:


if __name__ == "__main__":
    arr = [Item(60,10),Item(100,20),Item(120,30)]
    W = 50
    max_value = Knapsack(W,arr)
    print(max_value)


# In[ ]:





# In[ ]:




