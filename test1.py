%matplotlib notebook
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('./athletes.csv', parse_dates=['date_of_birth'])

df.head()


f = df[df['sex'] == 'female']

m = df[df['sex'] == 'male']

tennis_f = f[f['sport'] == 'tennis']
tennis_m = m[m['sport'] == 'tennis']
gym_f = f[f['sport'] == 'gymnastics']
gym_m = m[m['sport'] == 'gymnastics']

fig, ax = plt.subplots()
plots = [
    (tennis_f, 'silver', 'tennis, women'),
    (tennis_m, 'red', 'tennis, men'),
    (gym_f, 'gold', 'Gymnastics, women'),
    (gym_m, 'green', 'Gymnastics, men')
    
]

for df, color, label in plots:
    df.plot.scatter(ax=ax, x='weight', y='height', alpha=.25, color=color, label=label)
    
ax.set_xlabel('Weight (kg)')
ax.set_ylabel('Height (m)')
ax.set_title('height and weigh of olimpic athlethes')


fig, ax = plt.subplots()
gym_m.plot.scatter(ax=ax, x='height', y='weight', c='bronze', colormap='plasma')

plt.style.use('seaborn-pastel')

df = pd.read_csv('./sales.csv', parse_dates = ['Date'])

df.info()

df['month'] = df['Date'].dt.month
df.head()

g = df.groupby(['month', 'Product'])['Amount'].sum()
g = g.unstack()
revenue = g.fillna(0).cumsum()  # tutaj jest suma kumulacyjna (bierzemy poprzednie produkty i kazdy kolejny)
revenue

fig.ax = plt.subplots()
revenue.plot.area(title='Revenue 2019 (EUR)',ax=ax)

df = pd.read_csv('./athletes.csv')

top = df.groupby('nationality')[['gold', 'silver', 'bronze']]\
.sum().sort_values('gold', ascending=False)\
.head(10)
top

fig, ax = plt.subplots()
top.plot.bar(ax=ax, stacked=True, color=['gold', 'silver', 'brown'])
fig.tight_layout()
