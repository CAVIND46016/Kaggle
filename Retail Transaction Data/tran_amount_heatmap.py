import pandas as pd
import calendar
import matplotlib.pyplot as plt
import seaborn as sns

retail_data_response = pd.read_csv('Retail_Data_Response.csv') #customer_id  response
retail_data_trans = pd.read_csv('Retail_Data_Transactions.csv') # customer_id trans_date  tran_amount


retail_data_trans['trans_date'] = pd.to_datetime(retail_data_trans['trans_date'], format='%d-%b-%y')
retail_data_trans['year'] = retail_data_trans['trans_date'].apply(lambda x: x.year)
retail_data_trans['month'] = retail_data_trans['trans_date'].apply(lambda x: calendar.month_abbr[x.month])

revenue_agg = (retail_data_trans.groupby(by=['year', 'month'], as_index=False).sum()).pivot("month", "year", "tran_amount")

plt.figure(figsize=(9,9))
r = sns.heatmap(revenue_agg, cmap='BuPu')
r.set_title("Retail transaction amount heatmap from years 2011 - 2015")
plt.show()
