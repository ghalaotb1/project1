import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('countries.csv')
print(df.head())
df.plot(kind='bar', x='country', y='population')
plt.show()
