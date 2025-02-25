import pandas as pd

raw_file = pd.read_csv('raw_csv/5m Sales Records.csv', low_memory=False)
print('\ndf:\n',raw_file.sort_values(by=['Order Date'], ascending=True))

raw_file['Calendar Year'] = raw_file['Order Date'].str[-4:]
raw_file['Calendar Year'] = raw_file['Calendar Year'].astype(int)
print('\nraw_file:\n',raw_file.sort_values(by=['Order Date'], ascending=True))
raw_file.to_csv('raw_csv/5m Sales Records.csv', index=False)

total_orders_per_day = raw_file.groupby(['Order Date']).agg(
    units_sold = ('Units Sold','sum')
)
print('total orders per day\n',total_orders_per_day)
total_orders_per_day.to_csv('new_csvs/total_orders_per_day.csv')

for x in range(2010,2021):
    try:
        calendar_year = pd.read_csv('raw_csv/5m Sales Records.csv', low_memory=False)
        calendar_year = calendar_year.loc[calendar_year['Calendar Year'] == x]
        print(f'{x}_orders.csv')
        calendar_year.to_csv(f'new_csvs/{x}_orders.csv', index=False)
    except Exception as e:
        print(f'error - cannot filter rows accordingly - {type(e)}')