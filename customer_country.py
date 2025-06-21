import pandas as pd

default_path=r'C:\Users\Stephen_Gonzales1\Documents\AdvPython\IntrotoVSCode'

customer_country_data=pd.read_csv(default_path+r'\customers.csv')

print(customer_country_data.head())

customer_country_only=customer_country_data[['FirstName','LastName','Country']]

customer_country_only['FullName']=customer_country_only['FirstName']+' '+customer_country_only['LastName']


customer_country_only=customer_country_only[['FullName','Country']]

customer_country_only.to_csv(default_path+r'\customer_country.csv',index=False) 