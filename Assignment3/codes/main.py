import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import openpyxl
import os
os.chdir('C:\\Users\\ADMIN\\Documents')

df = pd.read_excel('Given_data.xlsx','Sheet1')
print(df)
df['A'] = np.arange(300,1000,100)
# Create bar plot
plt.bar(df['A']+50, df['No.of neon lamps'], width =100, color='blue', ec= 'black',alpha = 0.5)

# Add title and label the axes
plt.title('HISTOGRAM',fontsize=17);
plt.ylabel('No.of neon lamps')
plt.xlabel('Lifetime(in hrs)')
plt.show()

#neon lamps with lifetime more than 700 hours
wb = openpyxl.load_workbook('Given_data.xlsx')
sheet = wb['Sheet1']
sum = sheet['B6'].value + sheet['B7'].value + sheet['B8'].value 

print("No.of neon lamps that have a lifetime of more than 700 hours is", sum)
