#!/usr/bin/env python
# coding: utf-8

# In[88]:


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return self.value
        


# In[89]:


class Singly_Linked_list():
    def __init__(self):
        self.head = None
        
    def push(self ,value):
        #new node
        new_node = Node(value)
        if(self.head == None):
            self.head = new_node
            new_node.next = None
         
        temp = self.head
        while (temp.next is not None):
            temp = temp.next
        temp.next = new_node
        new_node.next = None
        return
      
        
    def pop(self):
        if(self.head == None):
            raise Exception("no items items in the list")
            return
        
        temp = self.head
        if(self.head.next is None):
            self.head = None
            return
        
        while(temp.next is not None):
            prev = temp
            temp = temp.next
        prev.next = None
        return
    
    def __str__(self):
        l = "[ "
        temp = self.head
        while temp is not None:
            l = l + str(temp.value) + ", "
            temp = temp.next
        l = l.rstrip(", ")
        l = l + " ]"
        return l


# In[90]:


n = Singly_Linked_list()
n.push(1)
n.push(2)
n.push(3)
n.push(4)
n.pop()
n.pop()
n.pop()
n.pop()




print(n)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




