import pandas as pd

default_path=r'C:\Users\Stephen_Gonzales1\Documents\AdvPython\IntrotoVSCode'

customer_sales_data=pd.read_csv(default_path+r'\sales.csv')

print(customer_sales_data.head())

customer_sales_grouped=customer_sales_data.groupby('CustomerID').agg(
    subtotal_sum=('SubTotal','sum'),
    tax_sum=('TaxAmt','sum'),
    freight_sum=('Freight','sum')
)

print(customer_sales_grouped.head())

customer_sales_final=customer_sales_grouped[['subtotal_sum','tax_sum','freight_sum']].reset_index()

customer_sales_final=customer_sales_final.assign(
    Customer=customer_sales_final['CustomerID'],
    Total=(customer_sales_final['subtotal_sum']+customer_sales_final['tax_sum']+customer_sales_final['freight_sum']).map('${:,.2f}'.format)
)

customer_sales_final=customer_sales_final[['Customer','Total']]

print(customer_sales_final.head())

customer_sales_final.to_csv(default_path+r'\salesreport.csv',index=False)