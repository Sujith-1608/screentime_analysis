#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[28]:


path="C:/Users/sujit/OneDrive/Desktop/Data Analysis Project/Dataset/screentime_analysis.csv"
data=pd.read_csv(path)


# In[29]:


data.head()


# In[30]:


data.columns


# In[31]:


data.tail()


# In[32]:


data.describe()


# In[45]:


print(data.isnull().sum())


# In[46]:


data.tail()


# In[48]:


data['Date']=pd.to_datetime(data['Date'])
print(data.dtypes)


# In[50]:


#Aggregate Metrics by Date
#Group the data by date to calculate total usage, notifications, and app openings for each day.
time_trends=data.groupby('Date').sum()
print(time_trends.head())


# In[55]:


plt.figure(figsize=(14, 6), dpi=100)

plt.plot(time_trends.index, time_trends['Usage (minutes)'], label='Usage (minutes)', marker='o', color='skyblue')
plt.plot(time_trends.index, time_trends['Notifications'], label='Notifications', marker='s', color='lightgreen')
plt.plot(time_trends.index, time_trends['Times Opened'], label='Times Opened', marker='^', color='salmon')

plt.title('Trends of Usage, Notifications, and Openings Over Time')
plt.xlabel('Date')
plt.ylabel('Count')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[59]:


# Set the style
sns.set(style="whitegrid")

# Plot trends for 'Usage (minutes)', 'Notifications', and 'Times Opened'
plt.figure(figsize=(14, 6), dpi=100)

sns.lineplot(x='Date', y='Usage (minutes)', data=time_trends, label='Usage (minutes)', color='skyblue')
sns.lineplot(x='Date', y='Notifications', data=time_trends, label='Notifications', color='lightgreen')
sns.lineplot(x='Date', y='Times Opened', data=time_trends, label='Times Opened', color='salmon')
plt.axvline(pd.Timestamp('2024-08-26'), color='red', linestyle='--', label='Most Used Date')


plt.title('Trends of Usage, Notifications, and Openings Over Time', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[63]:


fig, axes = plt.subplots(3, 1, figsize=(12, 12), dpi=100)

sns.lineplot(x='Date', y='Usage (minutes)', data=time_trends, ax=axes[0], color='#005082') 
sns.lineplot(x='Date', y='Notifications', data=time_trends, ax=axes[1], color='#006400') 
sns.lineplot(x='Date', y='Times Opened', data=time_trends, ax=axes[2], color='#8B0000')  

axes[0].set_title('Usage (minutes) Over Time', fontsize=14)
axes[1].set_title('Notifications Over Time', fontsize=14)
axes[2].set_title('Times Opened Over Time', fontsize=14)

for ax in axes:
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Count', fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()



# In[65]:


numeric_cols = time_trends.select_dtypes(include=['float64', 'int64'])
plt.figure(figsize=(8, 6))
sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Between Screen Time Metrics')
plt.show()


# In[67]:


sns.pairplot(numeric_cols)
plt.suptitle('Pairplot of Screen Time Metrics', y=1.02)
plt.show()


# In[68]:


plt.figure(figsize=(10, 6))
sns.boxplot(x=time_trends['Usage (minutes)'], color='skyblue')
plt.title('Boxplot of Daily Screen Time (minutes)')
plt.show()


# In[69]:


plt.figure(figsize=(10, 5))
sns.histplot(time_trends['Times Opened'], kde=True, bins=30, color='salmon')
plt.title('Distribution of Times Opened')
plt.xlabel('Times Opened')
plt.show()


# In[70]:


plt.figure(figsize=(10, 6))
sns.scatterplot(x='Usage (minutes)', y='Notifications', data=time_trends, hue='Times Opened', palette='viridis')
plt.title('Relationship Between Usage and Notifications')
plt.xlabel('Usage (minutes)')
plt.ylabel('Notifications')
plt.show()


# In[ ]:




