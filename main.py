import pandas as pd
import os

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

regions_list =  ['Asia','Australia and Oceania','Central America and the Caribbean','Europe','Middle East and North Africa','North America','Sub-Saharan Africa']
item_types_list =  ['Baby Food','Beverages','Cereal','Clothes','Cosmetics','Fruits','Household','Meat','Office Supplies','Personal Care','Snacks','Vegetables']
order_priorities_list =  ['C','H','L','M']
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
        # united states holiday orders - holidays on exact dates
        def united_states_of_america_holidays_exact_dates(df):
            try: 
                return df[(df['Country'] == 'United States of America') & ((df['Order Date'] == f"1/1/{year}") | (df['Order Date'] == f"2/12/{year}") |
                          (df['Order Date'] == f"6/19/{year}") | (df['Order Date'] == f"7/4/{year}") | (df['Order Date'] == f"10/31/{year}") | (df['Order Date'] == f"12/31/{year}"))]
            except Exception as e:
                print(f'cannot filter dataframes to holiday exact dates - e - {type(e)}')
        united_states_of_america_holidays_orders_1 = united_states_of_america_holidays_exact_dates(combined_raw_csvs)
        print(f'{year}_united_states_of_america_holiday_orders:\n:',united_states_of_america_holidays_orders_1)
        united_states_of_america_holidays_orders_1.to_csv(f'new_csvs/{year}_united_states_of_america_holiday_orders.csv', index=False)
        # united states holidays orders - holidays on non-exact dates (mlk day, president's day, memorial day, labor day, columbus/indigenous people's day, thanksgiving/turkey day)
        def united_states_of_america_holidays_non_exact_dates(df):
            try:
                return df[(df['Country'] == 'United States of America') & ((df['Order Date'] == "1/18/2010") | (df['Order Date'] == "1/17/2011") | 
                          (df['Order Date'] == "1/16/2012") | (df['Order Date'] == "1/21/2013") | (df['Order Date'] == "1/20/2014") | (df['Order Date'] == "1/19/2015") | 
                          (df['Order Date'] == "1/18/2016") | (df['Order Date'] == "1/16/2017") | (df['Order Date'] == "1/15/2018") | (df['Order Date'] == "1/21/2019") | 
                          (df['Order Date'] == "1/20/2020") | (df['Order Date'] == "2/15/2010") | (df['Order Date'] == "2/21/2011") | (df['Order Date'] == "2/20/2012") | 
                          (df['Order Date'] == "2/18/2013") | (df['Order Date'] == "1/17/2014") | (df['Order Date'] == "2/16/2015") | (df['Order Date'] == "2/15/2016") | 
                          (df['Order Date'] == "2/20/2017") | (df['Order Date'] == "2/19/2018") | (df['Order Date'] == "2/18/2019") | (df['Order Date'] == "2/17/2020") | 
                          (df['Order Date'] == "5/31/2010") | (df['Order Date'] == "5/30/2011") | (df['Order Date'] == "5/28/2012") | (df['Order Date'] == "5/27/2013") |
                          (df['Order Date'] == "5/26/2014") | (df['Order Date'] == "5/25/2015") | (df['Order Date'] == "5/30/2016") | (df['Order Date'] == "5/29/2017") | 
                          (df['Order Date'] == "5/28/2018") | (df['Order Date'] == "5/27/2019") | (df['Order Date'] == "5/25/2020") | (df['Order Date'] == "9/6/2010") | 
                          (df['Order Date'] == "9/5/2011") | (df['Order Date'] == "9/3/2012") | (df['Order Date'] == "9/2/2013") | (df['Order Date'] == "9/1/2014") | 
                          (df['Order Date'] == "9/7/2015") | (df['Order Date'] == "9/5/2016") | (df['Order Date'] == "9/4/2017") | (df['Order Date'] == "9/3/2018") | 
                          (df['Order Date'] == "9/2/2019") | (df['Order Date'] == "9/7/2020") | (df['Order Date'] == "10/11/2010") | (df['Order Date'] == "10/10/2011") | 
                          (df['Order Date'] == "10/8/2012") | (df['Order Date'] == "10/14/2013") | (df['Order Date'] == "10/13/2014") | (df['Order Date'] == "10/12/2015") | 
                          (df['Order Date'] == "10/10/2016") | (df['Order Date'] == "10/9/2017") | (df['Order Date'] == "10/8/2018") | (df['Order Date'] == "10/14/2019") | 
                          (df['Order Date'] == "10/12/2020") | (df['Order Date'] == "11/25/2010") | (df['Order Date'] == "11/24/2011") | (df['Order Date'] == "11/22/2012") | 
                          (df['Order Date'] == "11/28/2013") | (df['Order Date'] == "11/27/2014") | (df['Order Date'] == "11/26/2015") | (df['Order Date'] == "11/24/2016") | 
                          (df['Order Date'] == "11/23/2017") | (df['Order Date'] == "11/22/2018") | (df['Order Date'] == "11/28/2019") | (df['Order Date'] == "11/26/2020") )]
            except Exception as e:
                print(f'cannot filter dataframes to holiday non-exact dates - e - {type(e)}')
        united_states_of_america_holidays_orders_2 = united_states_of_america_holidays_non_exact_dates(orders)
        print(f'{year}_united_states_of_america_holiday_orders:\n:',united_states_of_america_holidays_orders_2)
        united_states_of_america_holidays_orders_2.to_csv(f'new_csvs/{year}_united_states_of_america_holiday_orders_2.csv', index=False)
        # combining dataframes containing orders on holidays in united states of america into a single dataframe
        united_states_of_america_holidays_orders_1_2010 = pd.read_csv('new_csvs/2010_united_states_of_america_holiday_orders.csv')
        united_states_of_america_holidays_orders_1_2011 = pd.read_csv('new_csvs/2011_united_states_of_america_holiday_orders.csv')
        united_states_of_america_holidays_orders_1_2012 = pd.read_csv('new_csvs/2012_united_states_of_america_holiday_orders.csv')
        united_states_of_america_holidays_orders_1_2013 = pd.read_csv('new_csvs/2013_united_states_of_america_holiday_orders.csv')
        united_states_of_america_holidays_orders_1_2014 = pd.read_csv('new_csvs/2014_united_states_of_america_holiday_orders.csv')
        united_states_of_america_holidays_orders_1_2015 = pd.read_csv('new_csvs/2015_united_states_of_america_holiday_orders.csv')
        united_states_of_america_holidays_orders_1_2016 = pd.read_csv('new_csvs/2016_united_states_of_america_holiday_orders.csv')
        united_states_of_america_holidays_orders_1_2017 = pd.read_csv('new_csvs/2017_united_states_of_america_holiday_orders.csv')
        united_states_of_america_holidays_orders_1_2018 = pd.read_csv('new_csvs/2018_united_states_of_america_holiday_orders.csv')
        united_states_of_america_holidays_orders_1_2019 = pd.read_csv('new_csvs/2019_united_states_of_america_holiday_orders.csv')
        united_states_of_america_holidays_orders_1_2020 = pd.read_csv('new_csvs/2020_united_states_of_america_holiday_orders.csv')
        united_states_of_america_holidays_orders_2_2010 = pd.read_csv('new_csvs/2010_united_states_of_america_holiday_orders_2.csv')
        united_states_of_america_holidays_orders_2_2011 = pd.read_csv('new_csvs/2011_united_states_of_america_holiday_orders_2.csv')
        united_states_of_america_holidays_orders_2_2012 = pd.read_csv('new_csvs/2012_united_states_of_america_holiday_orders_2.csv')
        united_states_of_america_holidays_orders_2_2013 = pd.read_csv('new_csvs/2013_united_states_of_america_holiday_orders_2.csv')
        united_states_of_america_holidays_orders_2_2014 = pd.read_csv('new_csvs/2014_united_states_of_america_holiday_orders_2.csv')
        united_states_of_america_holidays_orders_2_2015 = pd.read_csv('new_csvs/2015_united_states_of_america_holiday_orders_2.csv')
        united_states_of_america_holidays_orders_2_2016 = pd.read_csv('new_csvs/2016_united_states_of_america_holiday_orders_2.csv')
        united_states_of_america_holidays_orders_2_2017 = pd.read_csv('new_csvs/2017_united_states_of_america_holiday_orders_2.csv')
        united_states_of_america_holidays_orders_2_2018 = pd.read_csv('new_csvs/2018_united_states_of_america_holiday_orders_2.csv')
        united_states_of_america_holidays_orders_2_2019 = pd.read_csv('new_csvs/2019_united_states_of_america_holiday_orders_2.csv')
        united_states_of_america_holidays_orders_2_2020 = pd.read_csv('new_csvs/2020_united_states_of_america_holiday_orders_2.csv')        
        united_states_of_america_holidays_orders_csvs = pd.concat([united_states_of_america_holidays_orders_1_2010,united_states_of_america_holidays_orders_1_2011,
                                                                   united_states_of_america_holidays_orders_1_2012,united_states_of_america_holidays_orders_1_2013,
                                                                   united_states_of_america_holidays_orders_1_2014,united_states_of_america_holidays_orders_1_2015,
                                                                   united_states_of_america_holidays_orders_1_2016,united_states_of_america_holidays_orders_1_2017,
                                                                   united_states_of_america_holidays_orders_1_2018,united_states_of_america_holidays_orders_1_2019,
                                                                   united_states_of_america_holidays_orders_1_2020,united_states_of_america_holidays_orders_2_2010,
                                                                   united_states_of_america_holidays_orders_2_2011,united_states_of_america_holidays_orders_2_2012,
                                                                   united_states_of_america_holidays_orders_2_2013,united_states_of_america_holidays_orders_2_2014,
                                                                   united_states_of_america_holidays_orders_2_2015,united_states_of_america_holidays_orders_2_2016,
                                                                   united_states_of_america_holidays_orders_2_2017,united_states_of_america_holidays_orders_2_2018,
                                                                   united_states_of_america_holidays_orders_2_2019,united_states_of_america_holidays_orders_2_2020])
        united_states_of_america_holidays_orders_csvs.to_csv('new_csvs/united_states_of_america_holiday_orders_master.csv',index=False)
        # order priority - united states of america holiday orders
        for order_priority in order_priorities_list:
            united_states_of_america_holidays_orders_csvs = pd.read_csv('new_csvs/united_states_of_america_holiday_orders_master.csv')
        # annual orders by region
        for region in regions_list:
            try:
                orders_by_region = combined_raw_csvs.loc[combined_raw_csvs['Region'] == region]
                orders_by_region.to_csv(f'new_csvs/{region}_orders.csv',index=False)
                annual_orders_by_region = combined_raw_csvs.loc[(combined_raw_csvs['Region'] == region) & (combined_raw_csvs['Calendar Year'] == year)]
                annual_orders_by_region.to_csv(f'new_csvs/{year}_{region}_orders.csv',index=False)
                # specific items ordered by region annually
                for item_type in item_types_list:
                    try:
                        def filter(df):
                            try: 
                                return df[(df['Region'] == region) & (df['Calendar Year'] == year) & (df['Item Type'] == item_type)]
                            except Exception as e:
                                print(f'error - cannot filter rows accordingly - {type(e)}') 
                        item_type_orders_by_region_annually = filter(combined_raw_csvs)
                        print(f'{region} - {year} Orders - {item_type}:\n',item_type_orders_by_region_annually)
                    except Exception as e:
                        print(f'error - cannot filter rows accordingly - {type(e)}')                     
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
os.remove('new_csvs/Europe_orders.csv')
os.remove('new_csvs/Sub-Saharan Africa_orders.csv')