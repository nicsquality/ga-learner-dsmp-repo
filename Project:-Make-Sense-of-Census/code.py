# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record = np.array([50,  9,  4,  1,  0,  0, 40,  0])

#Code starts here
data_file = path # path for the file
data = np.genfromtxt(data_file, delimiter=",", skip_header=1)

print("\nData: \n\n", data)

print("\nType of data: \n\n", type(data))

census = np.concatenate((data, [new_record]), axis=0) 


# --------------
#Code starts here
age = census[:][:,0]
max_age = np.amax(age)
min_age = np.amin(age)
age_mean = np.mean(age)
age_std = np.std(age)



# --------------
#Code starts here
race_0 = census[census[:, 2] == 0]
race_1 = census[census[:, 2] == 1]
race_2 = census[census[:, 2] == 2]
race_3 = census[census[:, 2] == 3]
race_4 = census[census[:, 2] == 4]

len_0 = len(race_0) 
len_1 = len(race_1) 
len_2 = len(race_2) 
len_3 = len(race_3) 
len_4 = len(race_4) 

minority_race_list = [len_0, len_1, len_2, len_3, len_4]
print(minority_race_list)
minority_race_min = min(minority_race_list)
minority_race = minority_race_list.index(minority_race_min)
print(minority_race)


# --------------
#Code starts here
senior_citizens = census[census[:, 0] > 60]
working_hours_sum = np.sum(senior_citizens[:, 6])
senior_citizens_len = len(senior_citizens)
avg_working_hours = working_hours_sum / senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
high = census[census[:, 1] > 10]
low = census[census[:, 1] <= 10]

avg_pay_high = np.mean(high[:, 7])
avg_pay_low = np.mean(low[:, 7])

print(avg_pay_high)
print(avg_pay_low)


