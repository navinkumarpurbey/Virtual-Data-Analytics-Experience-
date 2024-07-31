#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Merging the data into one excel file using pandas
import pandas as pd


# In[2]:


reactions = pd.read_csv('Reactions.csv')
content = pd.read_csv('Content.csv')
reaction_types = pd.read_csv('ReactionTypes.csv')


# In[3]:


# Display the first few rows of each dataframe to understand their structure
reactions_head = reactions.head()
content_head = content.head()
reaction_types_head = reaction_types.head()


# In[4]:


(reactions_head, content_head, reaction_types_head)


# In[5]:


# Merge Reactions with Content on 'Content ID'
merged_df = pd.merge(reactions, content, on='Content ID', how='left')


# In[6]:


# Merge the result with ReactionTypes on 'Reactions Type'
final_df = pd.merge(merged_df, reaction_types, left_on='Reactions Type', right_on='ReactionType', how='left')


# In[7]:


# Check the merged result
final_df.head()


# In[8]:


# Group by 'Category' and calculate the total scores
category_scores = final_df.groupby('Category')['Score'].sum().reset_index()


# In[9]:


# Sort the categories by total score in descending order and select the top 5
top_5_categories = category_scores.sort_values(by='Score', ascending=False).head(5)


# In[10]:


top_5_categories


# In[ ]:




