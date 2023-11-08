#!/usr/bin/env python
# coding: utf-8

# In[47]:


def Fibonacci(n):
    ans = [0,1]
    if n<=0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return ans
    else:
        Fibo = Fibonacci(n-1)
        Fibo.append(Fibo[-1] + Fibo[-2])
    return Fibo
def term(N):
    fiboseries = Fibonacci(N)
    return fiboseries[-2]+fiboseries[-1]
def proof(N):
    l=0
    i=0
    fiboseries = Fibonacci(N)
    lhs = 0
    for i in range(N):
        lhs+=(fiboseries[i]*fiboseries[i])
    temp = term(N)
    rhs =  fiboseries[-1] * temp
    print(lhs)
    print(rhs)
    if lhs==rhs:
        print("PROVED")
    else:
        print("FAIL")


# In[48]:


N = int(input("Enter the no. of terms"))
print(f"Fibonacci of {N} numbers is : ")
ret = Fibonacci(N)
print(ret)
proof(N)


# In[ ]:




