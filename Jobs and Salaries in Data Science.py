#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Load your dataset
df = pd.read_csv('C:\\Users\\offic\\Documents\\jobs_in_data.csv')


# In[4]:


# Display the first few rows of the dataset to understand its structure
print(df.head())


# In[6]:


# Get a concise summary of the dataframe
print(df.info())


# In[8]:


# Descriptive statistics for numeric columns
print(df.describe())
# Method 1: Using astype() to convert to integers directly (if the conversion is safe)
df['work_year'] = df['work_year'].astype(int)
df['salary'] = df['salary'].astype(int)


# In[9]:


# Descriptive statistics for object (categorical) columns
print(df.describe(include=['object']))


# In[20]:


import seaborn as sns
import matplotlib.pyplot as plt

# Define the number of top job titles you want to display
N = 20

# Calculate the job title counts
job_title_counts = df['job_title'].value_counts()

# Filter the top N job titles
top_job_titles = job_title_counts.head(N).index

# Filter the DataFrame to include only the top N job titles
filtered_df = df[df['job_title'].isin(top_job_titles)]

# Create the plot
plt.figure(figsize=(10, 6))
sns.countplot(y='job_title', data=filtered_df, order=top_job_titles)
plt.title(f'Distribution of Top {N} Job Titles')
plt.show()


# Salary distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['salary'], bins=30, kde=True)
plt.title('Salary Distribution')
plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

# Define the number of top job titles you want to display
N = 20

# Calculate the job title counts
job_title_counts = df['job_title'].value_counts()

# Filter the top N job titles
top_job_titles = job_title_counts.head(N).index

# Filter the DataFrame to include only the top N job titles
filtered_df = df[df['job_title'].isin(top_job_titles)]

# Calculate the average salary for each of the top job titles
average_salary_by_title = filtered_df.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False)

# Create the plot
plt.figure(figsize=(10, 6))
sns.barplot(x=average_salary_by_title.values, y=average_salary_by_title.index)
plt.title(f'Average Salary for Top {N} Job Titles')
plt.xlabel('Average Salary')
plt.ylabel('Job Title')
plt.show()


# In[23]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming df is your DataFrame and it has columns 'JobTitle', 'Location', and 'Salary'

# Calculate the average salary per job title
avg_salary_by_job_title = df.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False)

# Calculate the average salary per location
avg_salary_by_location = df.groupby('employee_residence')['salary_in_usd'].mean().sort_values(ascending=False)

# Top 20 job titles by average salary
top_job_titles = avg_salary_by_job_title.head(20)

# Top 20 locations by average salary
top_locations = avg_salary_by_location.head(20)

# Set the aesthetics for the plots
sns.set(style="whitegrid")

# Plot for top 20 job titles by average salary
plt.figure(figsize=(10, 8))
sns.barplot(x=top_job_titles.values, y=top_job_titles.index, palette="Blues_d")
plt.title('Top 20 Job Titles by Average Salary')
plt.xlabel('Average Salary')
plt.ylabel('Job Title')
plt.show()

# Plot for top 20 locations by average salary
plt.figure(figsize=(10, 8))
sns.barplot(x=top_locations.values, y=top_locations.index, palette="Reds_d")
plt.title('Top 20 Locations by Average Salary')
plt.xlabel('Average Salary')
plt.ylabel('Employee Residence')
plt.show()


# In[29]:


import seaborn as sns
import matplotlib.pyplot as plt

# Assuming df is your DataFrame and it has columns 'job_title', 'work_setting', 'company_location', and 'salary_in_usd'

# Filter top job titles if necessary
top_job_titles = df['job_title'].value_counts().head(10).index
filtered_df = df[df['job_title'].isin(top_job_titles)]

# Set the aesthetics for the plots
sns.set(style="whitegrid")

# Create a box plot for salary distribution by work setting for different job titles
plt.figure(figsize=(20, 15))
sns.boxplot(x='salary_in_usd', y='job_title', hue='work_setting', data=filtered_df, palette='coolwarm')
plt.title('Salary Distribution by Work Setting for Different Job Titles')
plt.xlabel('Salary in USD')
plt.ylabel('Job Title')
plt.show()


# In[39]:


pip install squarify


# In[42]:


import pandas as pd

# Aggregate the data
job_counts = df.groupby(['job_category', 'job_title']).size().reset_index(name='counts')

# Sort the job titles by counts and get the top 20
top_job_counts = job_counts.sort_values('counts', ascending=False).head(20)


# In[62]:


import matplotlib.pyplot as plt
import squarify
import seaborn as sns

# Define a function to wrap text
def wrap_text(text, max_chars_per_line):
    words = text.split()
    wrapped_text = ""
    line_length = 0
    for word in words:
        if line_length + len(word) + 1 <= max_chars_per_line or line_length == 0:
            wrapped_text += word + " "
            line_length += len(word) + 1
        else:
            wrapped_text += "\n" + word + " "
            line_length = len(word) + 1
    return wrapped_text.strip()

# Use a Seaborn palette
palette = sns.color_palette('Dark2', n_colors=len(top_job_counts))

# Create labels that include both the job title and its count
labels = ["{} ({})".format(title, count) for title, count in zip(top_job_counts['job_title'], top_job_counts['counts'])]

# Wrap each label
max_chars_per_line = 10  # Set a suitable character limit for each line
wrapped_labels = [wrap_text(label, max_chars_per_line) for label in labels]

# Plotting
plt.figure(figsize=(15, 15))
squarify.plot(sizes=top_job_counts['counts'], label=wrapped_labels, alpha=0.8, color=palette, text_kwargs={'color':'white', 'fontsize':9})
plt.title('Treemap of Top 20 Job Titles within Job Categories', color='white')
plt.axis('off')
plt.show()


# In[ ]:




