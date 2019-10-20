# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path

#Code starts here 

data = pd.read_csv(path)

data.Gender.replace('-', 'Agender', inplace = True)

gender_count = data.Gender.value_counts()

gender_count.plot(kind = 'bar')
plt.title('Gender Count')
plt.xlabel('Gender')
plt.ylabel('Counts')
plt.show()


# --------------
#Code starts here

alignment = data.Alignment.value_counts()

alignment.plot(kind = 'pie')

plt.title('Character Alignment')
plt.show()


# --------------
#Code starts here

sc_df = data[['Strength','Combat']]

sc_covariance = sc_df.Strength.cov(sc_df.Combat)

sc_strength = sc_df.Strength.std()

sc_combat = sc_df.Combat.std()

sc_pearson = sc_covariance / (sc_strength * sc_combat)


ic_df = data[['Intelligence','Combat']]

ic_covariance = ic_df.Intelligence.cov(ic_df.Combat)

ic_intelligence = ic_df.Intelligence.std()

ic_combat = ic_df.Combat.std()

ic_pearson = ic_covariance / (ic_intelligence * ic_combat)



# --------------
#Code starts here

total_high = data.Total.quantile(0.99)

super_best = data[data.Total > total_high]

super_best_names = list(super_best.Name)

print(super_best_names)


# --------------
#Code starts here

fig, (ax_1, ax_2, ax_3) = plt.subplots(3)

data.Intelligence.plot(kind = 'box', ax = ax_1)
data.Speed.plot(kind = 'box', ax = ax_2)
data.Power.plot(kind = 'box', ax = ax_3)


