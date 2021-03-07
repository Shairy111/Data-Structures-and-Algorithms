#!/usr/bin/env python
# coding: utf-8

# In[58]:


class Queue():
    def __init__(self):
        self.size = 5
        self.list = list(range(0,self.size))
        self._in = 0
        self._out = 0
        self.is_empty = True
        self.is_full = False
     
    def _increment(self,index):
        if(index + 1 == self.size):
            return 0
        else:
            return index + 1
    
    def enqueue(self, value):
        if(self.is_full):
            raise Exception("queue is full")
            return
        self.list[self._in] = value
        self._in = self._increment(self._in)
        self.is_empty = False
        if(self._in == self._out):
            self.is_full = True
    
    def dequeue(self):
        if (self.is_empty):
            raise Exception("queue is already empty")
            return
        value = self.list[self._out]
        self.list[self._out] = 0
        print(self.list)
        self._out = self._increment(self._out)
        if(self._out == self._in):
            self.is_empty = True
        return value


# In[62]:


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())



# In[ ]:





# In[ ]:




