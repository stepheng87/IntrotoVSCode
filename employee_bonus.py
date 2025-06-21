import pandas as pd

default_path=r'C:\Users\Stephen_Gonzales1\Documents\AdvPython\IntrotoVSCode'

employee_data=pd.read_csv(default_path+r'\employee_data.csv')

print(employee_data.head())

employee_data_mod=employee_data[['Name','Salary','Bonus']]

bonus_amount=employee_data_mod['Salary']*employee_data_mod['Bonus']

total_pay=employee_data_mod['Salary']+bonus_amount

employee_data_mod=employee_data_mod.assign(
    Salary=employee_data_mod['Salary'].map('${:,.2f}'.format),
    Bonus=bonus_amount.map('${:,.2f}'.format),
    Pay=total_pay.map('${:,.2f}'.format)
)

print(employee_data_mod.head())

for x, row in employee_data_mod.iterrows():
    print(f"Name: {row['Name']}")
    print(f"Salary: {row['Salary']}")
    print(f"Bonus: {row['Bonus']}")
    print(f"Pay: {row['Pay']}")
    print()