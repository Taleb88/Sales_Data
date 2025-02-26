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
print('\ncombined_raw_csvs:\n',combined_raw_csvs.sort_values(by=['Order Date'],ascending=True))

combined_raw_csvs['Calendar Year'] = combined_raw_csvs['Order Date'].str[-4:]
combined_raw_csvs['Calendar Year'] = combined_raw_csvs['Calendar Year'].astype(int)

combined_raw_csvs.drop(["Unnamed: 0.2","Unnamed: 0.1","Unnamed: 0"],axis=1,inplace=True) # remove unncessary columns
print('\ncombined_raw_csvs:\n',combined_raw_csvs.sort_values(by=['Order Date'],ascending=True))

total_orders_per_day = combined_raw_csvs.groupby(['Order Date']).agg(
    units_sold = ('Units Sold','sum')
)
print('total orders per day:\n',total_orders_per_day)
total_orders_per_day.to_csv('new_csvs/total_orders_per_day.csv')

total_orders_per_year_per_country = combined_raw_csvs.groupby(['Country','Calendar Year']).agg(
    units_sold = ('Units Sold','sum')
)
print('total orders per year per country:\n',total_orders_per_year_per_country)
total_orders_per_year_per_country.to_csv('new_csvs/total_orders_per_year_per_country.csv')

total_orders_per_year_per_country_top_15 = total_orders_per_year_per_country.sort_values(by=['units_sold'],ascending=False).head(15)
print('total orders per year per country top 15:\n',total_orders_per_year_per_country_top_15)
total_orders_per_year_per_country_top_15.to_csv('new_csvs/total_orders_per_year_per_country_top_15.csv')

for year in range(2010,2021):
    try:
        calendar_year = combined_raw_csvs.loc[combined_raw_csvs['Calendar Year'] == year]
        calendar_year.to_csv(f'new_csvs/{year}_orders.csv', index=False)
        # orders by year
        orders = pd.read_csv(f'new_csvs/{year}_orders.csv')
        orders_total_profit_pivot_table = pd.pivot_table(orders,index=['Country'],columns=['Order Priority'],values=['Total Profit'],aggfunc='sum')
        print(f'{year}_orders_total_profit_pivot_table:\n',orders_total_profit_pivot_table)
        orders_total_profit_pivot_table.to_csv(f'new_csvs/{year}_orders_total_profit_per_country_pivot_table.csv')
        orders_average_profit_pivot_table = pd.pivot_table(orders,index=['Country'],columns=['Order Priority'],values=['Total Profit'],aggfunc='mean')
        print(f'{year}_orders_average_profit_pivot_table:\n',orders_average_profit_pivot_table)
        orders_average_profit_pivot_table.to_csv(f'new_csvs/{year}_orders_average_profit_per_country_pivot_table.csv')
    except Exception as e:
        print(f'error - cannot filter rows accordingly - {type(e)}')

print('\nRegion unique values:\n',combined_raw_csvs['Region'].unique())
print('\nCountry unique values:\n',combined_raw_csvs['Country'].unique())
print('\nItem Type unique values:\n',combined_raw_csvs['Item Type'].unique())
print('\nSales Channel unique values:\n',combined_raw_csvs['Sales Channel'].unique())
print('\nOrder Priority unique values:\n',combined_raw_csvs['Order Priority'].unique())
print('\nUnits Sold unique values:\n',combined_raw_csvs['Units Sold'].unique())
print('\nUnit Price unique values:\n',combined_raw_csvs['Unit Price'].unique())
print('\nUnit Cost unique values:\n',combined_raw_csvs['Unit Cost'].unique())
print('\nTotal Revenue unique values:\n',combined_raw_csvs['Total Revenue'].unique())
print('\nTotal Cost unique values:\n',combined_raw_csvs['Total Cost'].unique())
print('\nTotal Profit unique values:\n',combined_raw_csvs['Total Profit'].unique())