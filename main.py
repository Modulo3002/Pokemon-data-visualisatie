import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

# Data inladen
data = pd.read_csv ('pokemon.csv')
#print(data.head(n=10))

# Data schoonmaken
data.columns = data.columns.str.upper().str.replace('_', '')
#print(data.head())

data = data.drop(['#'], axis=1)
data = data.set_index ('NAME')
#print(data.head(n=10))
data.index = data.index.str.replace('.*(?=Mega)','')
data['TYPE 2'].fillna(data['TYPE 1'],inplace=True)
#print(data.head(n=10))

#print(data.loc['Meowth'])
#print(data.loc['Tentacruel'])
#print(data.loc['Pikachu'])
#print(data.loc['Goomy'])
#print(data[data['TYPE 1']=='Electric'])

#print('Max TOTAL: ', data['TOTAL'].idxmax())

#Data viz

bins=range(0,200,20)
plt.hist(data[data['GENERATION']==5]["ATTACK"], bins, histtype="bar", rwidth=1.2, color='#0ff0ff')
plt.xlabel('Attack')
plt.ylabel('Count')
plt.plot()
plt.axvline(data['ATTACK'].mean(),linestyle='dashed', color='green')
#plt.show()

gen1= data[data['GENERATION'] == 1]
legendary = data[data['LEGENDARY'] == True]

print(legendary[legendary['TYPE 1'] == 'Ice'].size / 11)

#plt.subplots(figsize = (15,5))
#sns.boxplots(x="TYPE 1", y="TOTAL", data = legendary)
#plt.show()

plt.subplots(figsize =(15,5))
sns.violinplot(x = "GENERATION", y = "TOTAL", data=data)
plt.show()