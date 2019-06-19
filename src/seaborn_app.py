import matplotlib.pyplot as plt # add this line if run outside jypiter nb
import seaborn as sns
sns.set()

tips = sns.load_dataset('tips')

# print(tips.head())

# sns.distplot(tips['total_bill'], kde=False, bins=30)
#kde kernel density estimation

# sns.jointplot(x='total_bill', y = 'tip', data = tips, kind = 'hex')

# sns.pairplot(tips, hue='sex')
#hex shows darker the grouping of data

sns.rugplot(tips['total_bill'])
plt.show() #for running outside JNB

flights = sns.load_dataset('flights')

flights.pivot_table(values='passengers',index='month',columns='year')

pvflights = flights.pivot_table(values='passengers',index='month',columns='year')
sns.heatmap(pvflights, cmap='magma',linecolor='white',linewidths=1)
plt.show() #for running outside JNB