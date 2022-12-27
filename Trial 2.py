
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\ghost\Downloads\Network_dataset_19.csv')
data['ts'] = pd.to_datetime(data['ts'], unit = 's')
df = pd.DataFrame(data, columns = ['ts', 'src_bytes'])

df['ts'] = pd.to_datetime(df['ts'])
df.index = df['ts']
del df['ts']

df.plot(figsize=(15,6))
for i:
    if i == '192.168.1.32'
plt.show()

'''
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\ghost\Downloads\Network_dataset_19.csv')
data['ts'] = pd.to_datetime(data['ts'], unit = 's')

print(df.loc['r4']['src_ip'])
print(df.loc['r4','src_ip'])
print(df.loc['r4'][1])
'''