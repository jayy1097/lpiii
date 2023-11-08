#!/usr/bin/env python
# coding: utf-8

# In[75]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.svm import SVC


# In[51]:


df = pd.read_csv("C:\\Users\\vedan\\OneDrive\\Documents\\dataset\\emails.csv")


# In[50]:


df
df.head()
df.describe()
df.shape
df.isnull().sum()
set(df.dtypes)
df.columns


# In[54]:


df.drop(['Email No.'],axis=1,inplace=True)


# In[62]:


x = df.drop(['Prediction'],axis=1)
y = df['Prediction']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=0)


# In[63]:


sc = StandardScaler()
x_test = sc.fit_transform(x_test)
x_train = sc.fit_transform(x_train)


# In[71]:


knn = KNeighborsClassifier(n_neighbors = 4)
knn.fit(x_train,y_train)
y_pred = knn.predict(x_test)


# In[83]:


print(accuracy_score(y_test,y_pred)*100)
print(confusion_matrix(y_test,y_pred))
y_test.value_counts()


# In[86]:


sv = SVC(kernel='linear')
sv.fit(x_train,y_train)
y_pred_sv = sv.predict(x_test)


# In[88]:


print(accuracy_score(y_test,y_pred_sv)*100)
print(confusion_matrix(y_test,y_pred_sv))
y_test.value_counts()


# In[ ]:




