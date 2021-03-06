#!/usr/bin/env python
# coding: utf-8

# In[28]:


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Shape:
    def __init__(self, point):
        self.point = point
        
    def move(self, point):
        self.point = point
        


# In[29]:


class Circle(Shape):
    def __init__(self, radius, centre_point):
        self.point = centre_point
        self.radius = radius
        self.area = 0
        
    def calculate_area(self):
        from math import pi
        self.area = 2 * pi * (self.radius ** 2)
        


# In[30]:


class Rectangle(Shape):
    def __init__(self, p1, length, width):
        self.point = p1
        self.length = length
        self.width = width


# In[31]:


class Line(Shape):
    def __init__(self, p1, p2):
        self.point = p1
        self.point2 = p2
        self.distance = 0
        
    def calculate_distance_formula(self):
        from math import sqrt
        n1 = (self.point2.x - self.point.x) ** 2
        n2 = (self.point2.y - self.point.y) ** 2
        self.distance = sqrt(n1 + n2)


# In[32]:


class Triangle(Shape):
    def __init__(self, p1, p2, p3, area):
        self.point = p1
        self.point2 = p2
        self.point3 = p3
        self.area = area


# In[ ]:




