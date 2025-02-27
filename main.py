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

print('\nRegion unique values:\n',combined_raw_csvs['Region'].sort_values(ascending=True).unique())
print('\nCountry unique values:\n',combined_raw_csvs['Country'].sort_values(ascending=True).unique())
print('\nItem Type unique values:\n',combined_raw_csvs['Item Type'].sort_values(ascending=True).unique())
print('\nSales Channel unique values:\n',combined_raw_csvs['Sales Channel'].sort_values(ascending=True).unique())
print('\nOrder Priority unique values:\n',combined_raw_csvs['Order Priority'].sort_values(ascending=True).unique())
print('\nUnits Sold unique values:\n',combined_raw_csvs['Units Sold'].sort_values(ascending=True).unique())
print('\nUnit Price unique values:\n',combined_raw_csvs['Unit Price'].sort_values(ascending=True).unique())
print('\nUnit Cost unique values:\n',combined_raw_csvs['Unit Cost'].sort_values(ascending=True).unique())
print('\nTotal Revenue unique values:\n',combined_raw_csvs['Total Revenue'].sort_values(ascending=True).unique())
print('\nTotal Cost unique values:\n',combined_raw_csvs['Total Cost'].sort_values(ascending=True).unique())
print('\nTotal Profit unique values:\n',combined_raw_csvs['Total Profit'].sort_values(ascending=True).unique())

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
        # annual orders by region
        regions_list =  ['Asia','Australia and Oceania','Central America and the Caribbean','Europe','Middle East and North Africa','North America','Sub-Saharan Africa']
        for region in regions_list:
            try:
                orders_by_region = combined_raw_csvs.loc[combined_raw_csvs['Region'] == region]
                orders_by_region.to_csv(f'new_csvs/{region}_orders.csv',index=False)
                annual_orders_by_region = combined_raw_csvs.loc[(combined_raw_csvs['Region'] == region) & (combined_raw_csvs['Calendar Year'] == year)]
                annual_orders_by_region.to_csv(f'new_csvs/{year}_{region}_orders.csv',index=False)
                # item type to be in third nested for loop
                item_types_list =  ['Baby Food','Beverages','Cereal','Clothes','Cosmetics','Fruits','Household','Meat','Office Supplies','Personal Care','Snacks','Vegetables']
                for item_type in item_types_list:
                    def filter(df):
                        try:
                            return df[(df['Region'] == region) & (df['Calendar Year'] == year) & (df['Item Type'] == item_type)]
                        except Exception as e:
                            print(f'cannot filter rows accordingly - {type(e)}')
                item_type_orders_by_region = filter(combined_raw_csvs)
                item_type_orders_by_region.to_csv(f'new_csvs/{year}_{region}_{item_type}_orders.csv',index=False)
            except Exception as e:
                print(f'error - cannot filter rows accordingly - {type(e)}')         
    except Exception as e:
        print(f'error - cannot filter rows accordingly - {type(e)}')

# split 2 csvs (new_csvs/Europe_orders.csv and new_csvs/Sub-Saharan Africa_orders.csv)
num_of_files = 2
num_of_rows = 650000
for x in range(num_of_files):
    europe_orders = pd.read_csv('new_csvs/Europe_orders.csv')
    sub_saharan_africa_orders = pd.read_csv('new_csvs/Sub-Saharan Africa_orders.csv')
    europe_orders_df = europe_orders[num_of_rows*x:num_of_rows*(x+1)]
    sub_saharan_africa_orders_df = sub_saharan_africa_orders[num_of_rows*x:num_of_rows*(x+1)]
    europe_orders_df.to_csv(f'new_csvs/Europe_orders_{x+1}.csv',index=False)
    sub_saharan_africa_orders_df.to_csv(f'new_csvs/Sub-Saharan Africa_orders_{x+1}.csv',index=False)

europe_orders_part_1 = pd.read_csv('new_csvs/Europe_orders_1.csv')
europe_orders_part_2 = pd.read_csv('new_csvs/Europe_orders_2.csv')
print('europe orders part 1:\n',europe_orders_part_1)
print('europe orders part 2:\n',europe_orders_part_2)
sub_saharan_africa_orders_part_1 = pd.read_csv('new_csvs/Sub-Saharan Africa_orders_1.csv')
sub_saharan_africa_orders_part_2 = pd.read_csv('new_csvs/Sub-Saharan Africa_orders_2.csv')
print('sub-saharan africa orders part 1:\n',sub_saharan_africa_orders_part_1)
print('sub-saharan africa orders part 2:\n',sub_saharan_africa_orders_part_2)

# remove combined csvs after splits
import os
os.remove('new_csvs/Europe_orders.csv')
os.remove('new_csvs/Sub-Saharan Africa_orders.csv')