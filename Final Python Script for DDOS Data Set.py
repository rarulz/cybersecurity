import pandas as pd
import matplotlib.pyplot as plt
#Read Data and narrow to columns of interest (Time Stamp, Source IP and
Source Bytes)
df = pd.read_csv('C:\Users\ghost\Downloads\Network_dataset_dataset_1.csv',
usecols=[0, 1, 8])
df.head()
#Convert 'ts' column to valid time stamp
df['ts'] = pd.to_datetime(df['ts'], unit='s')
print(df.head())
#Creating new data frame df1 where all rows are removed where source bytes
= zero.
# This enables eliminating unwanted rows
df1 = df.loc[~(df['src_bytes'] == 0)]
#this will show us the first 5 values of the new dataframe df1 we have
created.
print(df1.head())
#this will show us the last 5 values of the new dataframe df1 we have
created.
print(df1.tail())
#Adding a new column called cumulative source bytes where the rows are
organized by ip address
df1['ip_cum_src_bytes'] = df1[['src_ip',
'src_bytes']].groupby('src_ip').cumsum()
print(df1)
#New Data Frame Created where cleaned up data is grouped by Source IP
Address, same as above
df2 = df1.groupby('src_ip')
print(df2.head())
#filtering rows with a specific src IP Address
df3 = df1.query('src_ip.str.startswith("192.168.1.31")', engine="python")
print(df3)
#Time Series Plot of Data Frame 3 where we have filtered for a Specific IP
Address
df3.plot(figsize=(15, 5))
df3.plot(subplots=True, figsize=(15, 6))
df3.plot(x="ts", y="src_bytes", style='.')
plt.ylabel('Source Bytes')
plt.xlabel('Time Stamp')
plt.grid(True)
plt.ylim(0, 10000)
plt.show()