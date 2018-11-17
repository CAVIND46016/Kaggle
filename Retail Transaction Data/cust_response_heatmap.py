import pandas as pd
import calendar
import matplotlib.pyplot as plt
import seaborn as sns

retail_data_response = pd.read_csv('Retail_Data_Response.csv') #customer_id  response
retail_data_trans = pd.read_csv('Retail_Data_Transactions.csv') # customer_id trans_date  tran_amount

retail_data = pd.merge(retail_data_trans, retail_data_response, on='customer_id', how='left')
retail_data = retail_data[retail_data['response'] == 1]

retail_data['trans_date'] = pd.to_datetime(retail_data['trans_date'], format='%d-%b-%y')
retail_data['year'] = retail_data['trans_date'].apply(lambda x: x.year)
retail_data['month'] = retail_data['trans_date'].apply(lambda x: calendar.month_abbr[x.month])


response_agg = (retail_data.groupby(by=['year', 'month'], as_index=False).count()).pivot("month", "year", "response")

plt.figure(figsize=(9,9))
r = sns.heatmap(response_agg, cmap='BuPu')
r.set_title("Retail customer response heatmap from years 2011 - 2015")
plt.show()
