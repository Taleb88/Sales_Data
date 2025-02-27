# 2/27/2025 - IN PROGRESS
import pandas as pd

raw_csv_1 = pd.read_csv('raw_csvs/Sales Records - 1.csv',low_memory=False)
raw_csv_2 = pd.read_csv('raw_csvs/Sales Records - 2.csv',low_memory=False)
raw_csv_3 = pd.read_csv('raw_csvs/Sales Records - 3.csv',low_memory=False)
raw_csv_4 = pd.read_csv('raw_csvs/Sales Records - 4.csv',low_memory=False)
raw_csv_5 = pd.read_csv('raw_csvs/Sales Records - 5.csv',low_memory=False)
raw_csv_6 = pd.read_csv('raw_csvs/Sales Records - 6.csv',low_memory=False)
raw_csv_7 = pd.read_csv('raw_csvs/Sales Records - 7.csv',low_memory=False)
raw_csv_8 = pd.read_csv('raw_csvs/Sales Records - 8.csv',low_memory=False)
raw_csv_9 = pd.read_csv('raw_csvs/Sales Records - 9.csv',low_memory=False)
raw_csv_10 = pd.read_csv('raw_csvs/Sales Records - 10.csv',low_memory=False)

combined_raw_csvs = pd.concat([raw_csv_1,raw_csv_2,raw_csv_3,raw_csv_4,raw_csv_5,raw_csv_6,raw_csv_7,raw_csv_8,raw_csv_9,raw_csv_10])

# items order by year per country
regions_list =  ['Asia','Australia and Oceania','Central America and the Caribbean','Europe','Middle East and North Africa','North America','Sub-Saharan Africa']
item_types_list =  ['Baby Food','Beverages','Cereal','Clothes','Cosmetics','Fruits','Household','Meat','Office Supplies','Personal Care','Snacks','Vegetables']

for year in range(2010,2012):
    for region in regions_list:
        for item_type in item_types_list:
            def filter(df):
                return df[(df['Region'] == region) & (df['Calendar Year'] == year) & (df['Item Type'] == item_type)]
            item_type_orders_by_region = filter(combined_raw_csvs)
            item_type_orders_by_region.drop(["Unnamed: 0.2","Unnamed: 0.1","Unnamed: 0"],axis=1,inplace=True)
            print(f'{region} - {year} - {item_type} :\n',item_type_orders_by_region)

# 2/26/2025 - COMPLETE - SUCCESS
# import pandas as pd

# df1 = pd.read_csv('new_csvs/2010_Europe_orders.csv') # 1M + rows
# df2 = pd.read_csv('new_csvs/2010_Sub-Saharan Africa_orders.csv') # 1M+ rows

# print(df1,'\n')
# print(df2)

#=====================================================================================#