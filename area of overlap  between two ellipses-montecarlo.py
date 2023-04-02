#!/usr/bin/env python
# coding: utf-8

# In[14]:


import random
import math
import sys
import numpy as np
import matplotlib.pyplot as plt


# In[23]:


def plot_ellipse(a, b, x0, y0, theta):
    t = np.linspace(0, 2*np.pi, 100)
    ellipse = np.array([a*np.cos(t), b*np.sin(t)])
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    rotated_ellipse = rotation_matrix @ ellipse
    x = rotated_ellipse[0,:] + x0
    y = rotated_ellipse[1,:] + y0
    min_x=min(x)
    max_x=max(x)
    min_y=min(y)
    max_y=max(y)
    plt.plot(x, y)
    plt.gca().set_aspect('equal')
    return [min_x,max_x,min_y,max_y]


# In[24]:


def area_of_overlap(a1, b1, x1, y1, theta1, a2, b2, x2, y2, theta2, num_samples=1000):
    e1=plot_ellipse(a1, b1, x1, y1, theta1)
    e2=plot_ellipse(a2, b2, x2, y2, theta2)
    count = 0
    for i in range(num_samples):
        x = random.uniform(min(e1[0],e2[0]), max(e1[1],e2[1]))
        y = random.uniform(min(e1[2],e2[2]), max(e1[3],e2[3]))
        x1_new = (x-x1)*math.cos(-theta1) - (y-y1)*math.sin(-theta1) + x1
        y1_new = (x-x1)*math.sin(-theta1) + (y-y1)*math.cos(-theta1) + y1
        x2_new = (x-x2)*math.cos(-theta2) - (y-y2)*math.sin(-theta2) + x2
        y2_new = (x-x2)*math.sin(-theta2) + (y-y2)*math.cos(-theta2) + y2
        if ((x1_new-x1)**2/a1**2 + (y1_new-y1)**2/b1**2 <= 1) and ((x2_new-x2)**2/a2**2 + (y2_new-y2)**2/b2**2 <= 1):
            count += 1
            plt.scatter(x,y,c='r')
        elif (x1_new-x1)**2/a1**2 + (y1_new-y1)**2/b1**2 <= 1:
            plt.scatter(x,y,c='g')
        elif (x2_new-x2)**2/a2**2 + (y2_new-y2)**2/b2**2 <= 1:
            plt.scatter(x,y,c='b')
        else:
            plt.scatter(x,y,c='k')
    return ((count/num_samples)*(max(x1+a1, x2+a2)-min(x1-a1, x2-a2))*(max(y1+b1, y2+b2)-min(y1-b1, y2-b2)))


# In[25]:


# Example usage
area = area_of_overlap(2, 1, 0, 0, 0, 3, 2, 2, 0, 30, num_samples=100000)
print("Area of overlap:", area)


# In[ ]:




