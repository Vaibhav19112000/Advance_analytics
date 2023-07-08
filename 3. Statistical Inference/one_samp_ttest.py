import pandas as pd
from scipy.stats import ttest_1samp
df = pd.read_csv("PlantGrowth.csv")

### Two-Tailed Hypothesis
result = ttest_1samp(df['weight'], popmean=6, 
            alternative='two-sided')

test_stat = result[0]
p_value = result[1]
print("Test Statistic =", test_stat)
print("P - Value =", p_value)

# Conclusion: We reject H0 with alpha=0.05 or 0.01
# We often call it as 
# We reject H0 at 5% level of significance


### Lower tailed Hypothesis
result = ttest_1samp(df['weight'], popmean=6, 
            alternative='less')

test_stat = result[0]
p_value = result[1]
print("Test Statistic =", test_stat)
print("P - Value =", p_value)


### Upper tailed Hypothesis
result = ttest_1samp(df['weight'], popmean=6, 
            alternative='greater')

test_stat = result[0]
p_value = result[1]
print("Test Statistic =", test_stat)
print("P - Value =", p_value)

###############################
co2 = pd.read_csv("CO2.csv")

### Lower tailed Hypothesis
result = ttest_1samp(co2['uptake'], popmean=30, 
            alternative='less')

test_stat = result[0]
p_value = result[1]
print("Test Statistic =", test_stat)
print("P - Value =", p_value)

# Conclusion: We reject H0 at 5% level of significance
# The population mean uptake may be less than 30.
