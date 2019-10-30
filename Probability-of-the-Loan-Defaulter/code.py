# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)
total = len(df)

p_a = len(df[df.fico > 700]) / total

p_b = len(df[df.purpose == 'debt_consolidation']) / total

df1 = df[df.purpose == 'debt_consolidation']

p_a_b = len(df[(df.fico > 700) & (df.purpose == 'debt_consolidation')]) / total

result = p_a_b == p_a

print(result)

# code ends here


# --------------
# code starts here
prob_lp = len(df[df['paid.back.loan'] == 'Yes']) / total

prob_cs = len(df[df['credit.policy'] == 'Yes']) / total

new_df = df[df['paid.back.loan'] == 'Yes']

prob_pd_cs = (len(df[(df['paid.back.loan'] == 'Yes') & (df['credit.policy'] == 'Yes')]) / total) / prob_lp

bayes = (prob_pd_cs * prob_lp) / prob_cs

print(bayes)

# code ends here


# --------------
# code starts here
df.purpose.value_counts().plot(kind = 'bar')
plt.show()

df1 = df[df['paid.back.loan'] == 'No']

df1.purpose.value_counts().plot(kind = 'bar')
plt.show()
# code ends here


# --------------
# code starts here
inst_median = df.installment.median()

inst_mean = df.installment.mean()

df.installment.plot(kind = 'hist')
plt.show()

df['log.annual.inc'].plot(kind = 'hist')
plt.show()

# code ends here


