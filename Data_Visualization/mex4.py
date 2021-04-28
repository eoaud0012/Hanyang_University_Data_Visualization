#!/usr/bin/env python
# coding: utf-8

# In[21]:


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


# In[2]:


import mex1


# In[3]:


p2 = mex1.Cvalue()


# In[4]:


p2.add(11)


# In[5]:


p2.add(21)


# In[6]:


p2.add(31)


# In[7]:


p2.fprint()


# In[8]:


value = mex1.plus(10, 20)


# In[9]:


print(value)


# In[10]:


from mex1 import plus


# In[11]:


value = plus(10, 20)


# In[12]:


print(value)


# In[13]:


mex1.p1.add(31)


# In[14]:


mex1.p1.add(41)


# In[15]:


mex1.p1.add(51)


# In[16]:


mex1.p1.fprint()


# In[30]:


if __name__ == "__main__":
    p1 = Cvalue()
    p1.add(1)
    p1.add(2)
    p1.add(3)
    p1.fprint()


# In[ ]:





# In[ ]:




