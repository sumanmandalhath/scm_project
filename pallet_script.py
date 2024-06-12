#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


data =pd.read_csv("F:\Project 144\Dataset\pallet_Masked_fulldata.csv")
data


# In[9]:


data.dtypes


# In[8]:


data["Date"] = pd.to_datetime(data["Date"])
data["CustName"] = (data["CustName"]).astype(str)
data["WHName"] = (data["WHName"]).astype(str)


# # First Moment Business Decision - Measures of Central Tendency

# # Mean

# In[3]:


# Mean for Pallet Allot
data.loc[data['Transaction Type'] == 'Allot', 'QTY'].mean()


# In[4]:


# Mean for Pallet Return
data.loc[data['Transaction Type'] == 'Return', 'QTY'].mean()


# # Median

# In[6]:


# Median for Pallet Allot
data.loc[data['Transaction Type'] == 'Allot', 'QTY'].median()


# In[7]:


# Median for Pallet Return
data.loc[data['Transaction Type'] == 'Return', 'QTY'].median()


# # Mode

# In[8]:


# Mode for Pallet Allot
data.loc[data['Transaction Type'] == 'Allot', 'QTY'].mode()


# In[9]:


# Mode for Pallet Return
data.loc[data['Transaction Type'] == 'Return', 'QTY'].mode()


# # Second Moment Business Decision - Measures of Dispersion

# # Variance

# In[10]:


# Variance for Pallet Allot
data.loc[data['Transaction Type'] == 'Allot', 'QTY'].var()


# In[11]:


# Variance for Pallet Return
data.loc[data['Transaction Type'] == 'Return', 'QTY'].var()


# # Standard Deviation

# In[12]:


# Standard Deviation for Pallet Allot
data.loc[data['Transaction Type'] == 'Allot', 'QTY'].std()


# In[13]:


# Standard Deviation for Pallet Return
data.loc[data['Transaction Type'] == 'Return', 'QTY'].std()


# # Range

# In[14]:


# Range for Pallet Allot
range = max(data.loc[data['Transaction Type'] == 'Allot', 'QTY']) - min(data.loc[data['Transaction Type'] == 'Allot', 'QTY']) 
range


# In[4]:


# Range for Pallet Return
range1 = max(data.loc[data['Transaction Type'] == 'Return', 'QTY']) - min(data.loc[data['Transaction Type'] == 'Return', 'QTY']) 
range1


# # Third Moment Business Decision - Skewness

# In[16]:


data.loc[data['Transaction Type'] == 'Allot', 'QTY'].skew()


# In[17]:


data.loc[data['Transaction Type'] == 'Return', 'QTY'].skew()


# # Fourth Moment Business Decision - Kurtosis

# In[3]:


data.loc[data['Transaction Type'] == 'Allot', 'QTY'].kurt()


# In[4]:


data.loc[data['Transaction Type'] == 'Return', 'QTY'].kurt()


# # Graphical representation

# In[6]:


data.QTY.kurt()


# # 1. Univariate analysis

# In[6]:


plt.hist(data.QTY)
plt.show()
# Histogram shows the distribution slightly left skewed


# In[3]:


plt.boxplot(data.QTY)
plt.show()
# Boxplot shows that there are no potential outliers


# In[8]:


agg_df = data.groupby('Region')['QTY'].sum().reset_index()
plt.bar(agg_df['Region'], agg_df['QTY'], color=['blue' if q >= 0 else 'red' for q in agg_df['QTY']])
plt.xlabel('Region')
plt.ylabel('Total Quantity (QTY)')
plt.title('Total Quantity by Region')
plt.show()
# Bar plot shows that the East region has lowest order QTY and West has the highest


# In[16]:


data['Year'] = data['Date'].dt.year
agg_data1 = data.groupby('Year')['QTY'].sum().reset_index()
plt.figure(figsize=(10, 6))
plt.plot(agg_data1['Year'], agg_data1['QTY'], marker='o')
plt.title('Total Quantity Ordered Year-wise')
plt.xlabel('Year')
plt.ylabel('Total Quantity Ordered')
plt.grid(True)
plt.show()
# We can see that the trend of quantity ordered is going down with 2019 being the highest and lowest for 2023.


# # AutoEDA

# # 1. Sweetviz

# In[19]:


pip install sweetviz


# In[14]:


import sweetviz as sv


# In[15]:


s = sv.analyze(data)
s.show_notebook()


# # 2. Autoviz

# In[24]:


pip install autoviz


# In[16]:


from autoviz.AutoViz_Class import AutoViz_Class

av = AutoViz_Class()
a = av.AutoViz("F:\Project 144\Dataset\pallet_Masked_fulldata.csv")


# # 3. D-Tale

# In[26]:


pip install dtale


# In[27]:


import dtale


# In[29]:


#d = dtale.show(data)
#d.open_browser()
dtale.show(data, notebook=True)


# In[ ]:





# In[ ]:




