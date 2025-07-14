import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('countries.csv')
print('كل البيانات:')
print(df)
print('عدد الدول:', len(df))
print('إجمالي عدد السكان:', df['population'].sum())
print('متوسط عدد السكان:', df['population'].mean())
print('أكبر دولة سكاناً:', df.loc[df['population'].idxmax(), 'country'])
df.plot(kind='bar', x='country', y='population')
plt.title('عدد السكان لكل دولة')
plt.xlabel('الدولة')
plt.ylabel('عدد السكان')
plt.show()
