'''importing libraries'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('dark_background')

df = pd.read_csv(r'C:\Users\Chris\Documents\GitHub\python\Recruitment dataset\recruitment_data.csv')

'''EDA'''

# fig = plt.figure(figsize = (14, 14))
# ax = fig.add_subplot(221)
# sns.violinplot(x = 'status', y = 'ssc_p', data = df)
# ax.set_title('Violin Plot of Secondary Education Percentage vs Employablity Status')


# fig = plt.figure(figsize = (14, 14))
# ax = fig.add_subplot(221)
# sns.violinplot(x = 'status', y = 'hsc_p', data = df)
# ax.set_title('Violin Plot of Higher Secondary Education Percentage vs Employablity Status')


# fig = plt.figure(figsize = (14, 14))
# ax = fig.add_subplot(221)
# sns.violinplot(x = 'status', y = 'degree_p', data = df)
# ax.set_title('Violin Plot of Degree Percentage vs Employablity Status')


# fig = plt.figure(figsize = (14, 14))
# ax = fig.add_subplot(221)
# sns.violinplot(x = 'status', y = 'etest_p', data = df)
# ax.set_title('Violin Plot of Employability Test percentage vs Employablity Status')


# fig = plt.figure(figsize = (14, 14))
# ax = fig.add_subplot(221)
# sns.violinplot(x = 'status', y = 'mba_p', data = df)
# ax.set_title('Violin Plot of MBA Percentage vs Employablity Status')





# df_encoded = pd.get_dummies(data = df, prefix = 'OHE', prefix_sep='_', 
#                             columns = ['specialisation','workex', 'degree_t', 'gender', 'ssc_b', 'hsc_b', 'hsc_s'], 
#                             drop_first =True, dtype='int8')

# df.plot(x="specialisation", y="status", kind="bar")











