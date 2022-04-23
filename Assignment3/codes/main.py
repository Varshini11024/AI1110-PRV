import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Input parameters from excel file 
df= pd.read_excel(r'https://github.com/Varshini11024/AI1110-PRV/blob/main/Assignment3/Tables/Given_data.xlsx?raw=true')
print(df)

df['A'] = np.arange(300,1000,100)
# Create bar plot
plt.bar(df['A']+50, df['No.of neon lamps'], width =100, color='blue', ec= 'black',alpha = 0.5)

# Add title and label the axes
plt.title('HISTOGRAM',fontsize=17);
plt.ylabel('No.of neon lamps')
plt.xlabel('Lifetime(in hrs)')
plt.show()

sum=0
data = df['No.of neon lamps']

#The lifetime greater than 700 hours is from the range(4,7) in the given frequency table
sum = data[4]+data[5]+data[6]

print("No.of neon lamps that have a lifetime of more than 700 hours is", sum)
