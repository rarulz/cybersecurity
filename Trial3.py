from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\ghost\Downloads\Network_dataset_19.csv')
data['ts'] = pd.to_datetime(data['ts'], unit = 's')


index_labels=['r1','r2','r3','r4','r5']
df = pd.DataFrame(data, columns = ['ts', 'src_ip', 'src_bytes'])
print (df)
print (df['src_ip'].where(df['src_ip'] == '192.168.1.32'))

'''
print(data.loc['r4']['src_ip'])
print(data.loc['r4','src_ip'])
print(data.loc['r4'][1])
'''