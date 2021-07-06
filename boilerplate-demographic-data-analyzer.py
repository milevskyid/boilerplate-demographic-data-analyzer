#!/usr/bin/env python
# coding: utf-8

# In[114]:


import pandas as pd


# In[115]:


df = pd.read_csv('/Users/pro/Downloads/adult.data.csv')
df.head()


# In[116]:


df.info()


# In[118]:


race_count = df['race'].value_counts()
race_count


# In[119]:


average_age_men = df.loc[df['sex'] == "Male", ['age']].mean().round(1).iloc[0]
average_age_men


# In[120]:


percentage_bachelors = round(df.loc[df['education'] == 'Bachelors'].shape[0]*100 / df['education'].shape[0], 1)

percentage_bachelors 


# In[121]:


higher_education = df.groupby(['education', 'salary'])     .agg({'sex':'count'})     .rename(columns={'sex':'percentage'})     .query('education == ["Bachelors", "Masters", "Doctorate"]')     .transform(lambda x: 100*x/x.sum())     .query('salary == ">50K"')     .sum()     .round(1).iloc[0]
higher_education


# In[122]:


lower_education = df.groupby(['education', 'salary'])     .agg({'sex':'count'})     .rename(columns={'sex':'percentage'})     .query('education != ["Bachelors", "Masters", "Doctorate"]')     .transform(lambda x: 100*x/x.sum())     .query('salary == ">50K"')     .sum()     .round(1).iloc[0]
lower_education


# In[123]:


min_work_hours = df['hours-per-week'].min()
min_work_hours


# In[124]:


num_min_workers = df.loc[df['hours-per-week'] == 1, ['salary']]     .value_counts()     .transform(lambda x: 100*x/x.sum())     .round()     .min() 

num_min_workers


# In[125]:


highest_earning_country = df.groupby(['salary','native-country'])     .agg({'age':'count'})     .groupby(['native-country'])     .transform(lambda x: 100*x/x.sum())     .reset_index()     .query('salary == ">50K"')     .sort_values(by=['age'], ascending=False)     .iloc[0,1]
highest_earning_country


# In[126]:


highest_earning_country_percentage = df.groupby(['salary','native-country'])     .agg({'age':'count'})     .groupby(['native-country'])     .transform(lambda x: 100*x/x.sum())     .reset_index()     .query('salary == ">50K"')     .sort_values(by=['age'], ascending=False)     .iloc[0,2]     .round(1)
highest_earning_country_percentage


# In[127]:


df.loc[df['native-country'] == "India", ['occupation','age']]     .groupby('occupation')     .agg({'age':'count'})     .reset_index()     .sort_values(by=['age'], ascending=False)     .iloc[0,0] 

