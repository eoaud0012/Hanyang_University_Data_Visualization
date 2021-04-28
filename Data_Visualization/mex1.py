#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Cvalue:
    def __init__(self):
        self.lista=[]
    def add(self, num):
        self.lista.append(num)
    def fprint(self):
        print(self.lista)


# In[5]:


def plus(a, b):
    c = a + b
    return c


# In[6]:


p1 = Cvalue()


# In[7]:


p1.add(1)


# In[8]:


p1.add(2)


# In[9]:


p1.add(3)


# In[10]:


p1.fprint()


# In[ ]:





# In[ ]:




