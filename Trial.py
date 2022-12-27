import pandas as pd

df = pd.read_csv(r'C:\Users\ghost\Downloads\Network_dataset_19.csv', usecols=[0,1,2,8])
#Read dataset and filter columns that need to be used on time series
'''
print(df.head())
print(df.tail())
'''


df['ts'] = pd.to_datetime(df['ts'], unit = 's')
#Step 5 extra credit - converting timestamp into human readable format

print(df.head())
#this will show us the first 5 values of the dataframe we have created.

print(df.tail())
#this will show us the last 5 values of the dataframe we have created.

df1 = (df.drop_duplicates(['ts','src_bytes']).groupby(['ts'],as_index=True, sort=False)['src_bytes'].sum())
#Attempting to remove duplicates and totaling src bytes by ip address in a new dataframe df1

print(df1.head())
#this will show us the first 5 values of the new dataframe df1 we have created.

print(df1.tail())
#this will show us the last 5 values of the new dataframe df1 we have created.

'''
index_labels=['r1','r2','r3','r4','r5']
df2 = pd.DataFrame(df1, columns = ['ts', 'src_ip', 'src_bytes'])
print (df2)
print (df2['src_ip'].where(df2['src_ip'] == '192.168.1.32'))
'''

import matplotlib.pyplot as plt
import seaborn as sns

#df1.plot(figsize=(15,5))
#df1.plot(subplots=True, figsize=(15,6))
df1.plot(x="ts", y="src_bytes", style='.')
plt.ylabel('Source Bytes')
plt.xlabel('Time Period')
plt.grid(True)
plt.ylim(0,10000)
plt.show()

sns.set(rc={'figure.figsize':(11, 4)})
df1['ts'].plot(linewidth=0.5);
plt.show()

import matplotlib.pyplot as plt
df1['ts'] = pd.to_datetime(df1['ts'])
df1.index = df1['ts']
del df1['ts']
df1.plot(figsize=(15,6))
plt.show()
##print(df.head())

'''
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(rc={'figure.figsize':(11, 4)})
df1['ts'].plot(linewidth=0.5);
'''