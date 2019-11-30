# --------------
import pandas as pd

data = pd.read_csv(path)

data.Rating.hist()

data = data[data['Rating'] <= 5]

data.Rating.hist()



# --------------
# code starts here
total_null = data.isnull().sum()

percent_null = total_null / data.isnull().count()

missing_data = pd.concat([total_null, percent_null], axis = 1, keys=['Total','Percent'])

print(missing_data)

data.dropna(inplace = True)

total_null_1 = data.isnull().sum()

percent_null_1 = total_null / data.isnull().count()

missing_data_1 = pd.concat([total_null_1, percent_null_1], axis = 1, keys=['Total','Percent'])

print(missing_data_1)


# code ends here


# --------------

#Code starts here
import matplotlib.pyplot as plt
import seaborn as sns

ca = sns.catplot(x="Category",y="Rating",data=data, kind="box", height = 10)
ca.set_xticklabels(rotation=90)
plt.title('Rating vs Category [BoxPlot]')



#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here
print(data.Installs.value_counts())

data['Installs'] = data['Installs'].str.replace('+', '').str.replace(',', '').astype(int)

le = LabelEncoder()

data['Installs'] = le.fit_transform(data['Installs'])

sns.regplot(x="Installs", y="Rating", data=data)

plt.title('Rating vs Installs [RegPlot]')

#Code ends here



# --------------
#Code starts here
print(data.Price.value_counts())

data.Price = data.Price.str.replace('$', '').astype(float)

sns.regplot(x="Price", y="Rating", data=data)

plt.title('Rating vs Price [RegPlot]')

#Code ends here


# --------------

#Code starts here
print(data.Genres.unique())

data['Genres'] = data['Genres'].apply(lambda x : x.split(';')[0])

gr_mean = data[['Genres', 'Rating']].groupby(['Genres'], as_index = False).mean()

gr_mean.describe()

gr_mean = gr_mean.sort_values('Rating', axis = 0)

print(gr_mean.head(1))
print(gr_mean.tail(1))

#Code ends here


# --------------

#Code starts here
from datetime import datetime,date

print(data['Last Updated'])

data['Last Updated']=pd.to_datetime(data['Last Updated'])

max_date=max(data['Last Updated'])

data['Last Updated Days']=(max_date-data['Last Updated']).dt.days

sns.regplot(x="Last Updated Days", y="Rating", data=data)

plt.title('Rating vs "Last Updated Days" [RegPlot]')

#Code ends here


