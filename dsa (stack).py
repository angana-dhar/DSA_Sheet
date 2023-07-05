#!/usr/bin/env python
# coding: utf-8

# In[10]:


s = []
s.append('https://www.cnn.com/')
s.append('https://www.cnn.com/world')
s.append('https://www.cnn.com/india')
s.append('https://www.cnn.com/china')


# In[11]:


s[-1]


# In[3]:


s


# In[4]:


s.pop()


# In[5]:


s


# In[6]:


s.pop()


# In[7]:


s


# In[12]:


from collections import deque
stack = deque()


# In[13]:


dir(stack)


# In[15]:


stack.append('https://www.cnn.com/')


# In[16]:


stack


# In[17]:


class stack :
    def __init__(self):
        self.container = deque()
    def push(self,data):
        self.container.append(data)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container)==0
    def size(self):
        return len(self.container)


# In[18]:


s=stack()
s.push(8)


# In[19]:


s.peek()


# In[20]:


s.peek()


# In[21]:


s.pop()


# In[22]:


s


# In[23]:


s.is_empty()


# In[24]:


s.push(89)
s.push(123)
s.push(897)
s.push(873)


# In[26]:


stack()


# In[27]:


s.size()


# In[ ]:




