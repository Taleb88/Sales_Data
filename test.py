# 3/10/2025 - COMPLETE - SUCCESS - TO BE IMPLEMENTED
import pandas as pd
import csv

new_csv_data = []
for year in range(2010,2021):
    dfs = f'new_csvs/{year}_united_states_of_america_holiday_orders.csv'
    with open(dfs) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            new_csv_data.append([year,row['Region'],row['Country'],row['Item Type'],row['Sales Channel'],row['Order Priority'],row['Order Date'],row['Order ID'],
                                 row['Ship Date'],row['Units Sold'],row['Unit Price'],row['Unit Cost'],row['Total Revenue'],row['Total Cost'],row['Total Profit'],row['Calendar Year']
                                 ])
# write to new csv with combined data
with open('test.csv','w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Region','Country','Item Type','Sales Channel','Order Priority','Order Date','Order ID','Ship Date','Units Sold','Unit Price','Unit Cost','Total Revenue',
                     'Total Cost','Total Profit','Calendar Year'
                    ])
    writer.writerows(new_csv_data)

# # 3/10/2025 - COMPLETE - SUCCESS - TO BE IMPLEMENTED
# import pandas as pd

# raw_csv_1 = pd.read_csv('raw_csvs/Sales Records - 1.csv',low_memory=False)
# raw_csv_2 = pd.read_csv('raw_csvs/Sales Records - 2.csv',low_memory=False)
# raw_csv_3 = pd.read_csv('raw_csvs/Sales Records - 3.csv',low_memory=False)
# raw_csv_4 = pd.read_csv('raw_csvs/Sales Records - 4.csv',low_memory=False)
# raw_csv_5 = pd.read_csv('raw_csvs/Sales Records - 5.csv',low_memory=False)
# raw_csv_6 = pd.read_csv('raw_csvs/Sales Records - 6.csv',low_memory=False)
# raw_csv_7 = pd.read_csv('raw_csvs/Sales Records - 7.csv',low_memory=False)
# raw_csv_8 = pd.read_csv('raw_csvs/Sales Records - 8.csv',low_memory=False)
# raw_csv_9 = pd.read_csv('raw_csvs/Sales Records - 9.csv',low_memory=False)
# raw_csv_10 = pd.read_csv('raw_csvs/Sales Records - 10.csv',low_memory=False)

# combined_raw_csvs = pd.concat([raw_csv_1,raw_csv_2,raw_csv_3,raw_csv_4,raw_csv_5,raw_csv_6,raw_csv_7,raw_csv_8,raw_csv_9,raw_csv_10])

# for year in range(2010,2021):
#     def united_states_of_america_holidays(df):
#         try: 
#             return df[(df['Country'] == 'United States of America') & ((df['Order Date'] == f"1/1/{year}") | (df['Order Date'] == f"2/12/{year}") |
#                       (df['Order Date'] == f"6/19/{year}") | (df['Order Date'] == f"7/4/{year}") | (df['Order Date'] == f"10/31/{year}") | (df['Order Date'] == f"12/31/{year}"))]
#         except Exception as e:
#             print(f'cannot filter dataframes to contain holiday values only - e - {type(e)}')
#     united_states_of_america_holidays_orders = united_states_of_america_holidays(combined_raw_csvs)
#     print(f'{year}_united_states_of_america_holiday_orders:\n:',united_states_of_america_holidays_orders)
#     united_states_of_america_holidays_orders.to_csv(f'new_csvs/{year}_united_states_of_america_holiday_orders.csv', index=False)

# 2/27/2025 - COMPLETE - SUCCESS
# import pandas as pd

# raw_csv_1 = pd.read_csv('raw_csvs/Sales Records - 1.csv',low_memory=False)
# raw_csv_2 = pd.read_csv('raw_csvs/Sales Records - 2.csv',low_memory=False)
# raw_csv_3 = pd.read_csv('raw_csvs/Sales Records - 3.csv',low_memory=False)
# raw_csv_4 = pd.read_csv('raw_csvs/Sales Records - 4.csv',low_memory=False)
# raw_csv_5 = pd.read_csv('raw_csvs/Sales Records - 5.csv',low_memory=False)
# raw_csv_6 = pd.read_csv('raw_csvs/Sales Records - 6.csv',low_memory=False)
# raw_csv_7 = pd.read_csv('raw_csvs/Sales Records - 7.csv',low_memory=False)
# raw_csv_8 = pd.read_csv('raw_csvs/Sales Records - 8.csv',low_memory=False)
# raw_csv_9 = pd.read_csv('raw_csvs/Sales Records - 9.csv',low_memory=False)
# raw_csv_10 = pd.read_csv('raw_csvs/Sales Records - 10.csv',low_memory=False)

# combined_raw_csvs = pd.concat([raw_csv_1,raw_csv_2,raw_csv_3,raw_csv_4,raw_csv_5,raw_csv_6,raw_csv_7,raw_csv_8,raw_csv_9,raw_csv_10])

# # items order by year per country
# regions_list =  ['Asia','Australia and Oceania','Central America and the Caribbean','Europe','Middle East and North Africa','North America','Sub-Saharan Africa']
# item_types_list =  ['Baby Food','Beverages','Cereal','Clothes','Cosmetics','Fruits','Household','Meat','Office Supplies','Personal Care','Snacks','Vegetables']

# for year in range(2010,2012):
#     for region in regions_list:
#         for item_type in item_types_list:
#             def filter(df):
#                 return df[(df['Region'] == region) & (df['Calendar Year'] == year) & (df['Item Type'] == item_type)]
#             item_type_orders_by_region = filter(combined_raw_csvs)
#             print(f'{region} - {year} - {item_type} :\n',item_type_orders_by_region)

# 2/26/2025 - COMPLETE - SUCCESS
# import pandas as pd

# df1 = pd.read_csv('new_csvs/2010_Europe_orders.csv') # 1M + rows
# df2 = pd.read_csv('new_csvs/2010_Sub-Saharan Africa_orders.csv') # 1M+ rows

# print(df1,'\n')
# print(df2)

#=====================================================================================#