import pandas as pd
import zipfile

# Get the data from the archives
oil_and_wti_zipfile = zipfile.ZipFile('../task/datasets/oil-prices.zip')
population_zipfile = zipfile.ZipFile('../task/datasets/population.zip')
ppp_zipfile = zipfile.ZipFile('../task/datasets/ppp.zip')

# Store it in new folder 'data'
oil_and_wti_zipfile.extract('oil-prices-master/data/brent-year.csv', '../data/')
oil_and_wti_zipfile.extract('oil-prices-master/data/wti-year.csv', '../data/')
oil_and_wti_zipfile.close()
population_zipfile.extract('population-master/data/population.csv', '../data/')
population_zipfile.close()
ppp_zipfile.extract('ppp-master/data/ppp-gdp.csv', '../data/')
ppp_zipfile.close()

# Read the data
oil_prices_df = pd.read_csv('../data/oil-prices-master/data/brent-year.csv')
wti_df = pd.read_csv('../data/oil-prices-master/data/wti-year.csv')
population_df = pd.read_csv('../data/population-master/data/population.csv')
ppp_df = pd.read_csv('../data/ppp-master/data/ppp-gdp.csv')

# Adjusting the date format for oil prices
oil_prices_df['Date'] = pd.to_datetime(oil_prices_df.Date)
oil_prices_df['Date'] = oil_prices_df['Date'].dt.strftime('%Y')

# Adjusting the date format for wti
wti_df['Date'] = pd.to_datetime(wti_df.Date)
wti_df['Date'] = wti_df['Date'].dt.strftime('%Y')

# Adjusting the date format for population
population_df['Year'] = pd.to_datetime(population_df.Year, format='%Y')
population_df['Year'] = population_df['Year'].dt.strftime('%Y')

# Adjusting the date format for purchasing power parities
ppp_df['Year'] = pd.to_datetime(ppp_df.Year, format='%Y')
ppp_df['Year'] = ppp_df['Year'].dt.strftime('%Y')

def new_format(data, path):
    # Save data in 3 new formats
    data.to_csv(f'{path}.csv', index=False)
    data.to_excel(f'{path}.xlsx', index=False)
    data.to_json(f'{path}.json', orient='table', index=False)

# Save data in new formats
new_format(oil_prices_df, '../data/oil-prices-master/data/brent-year')
new_format(wti_df, '../data/oil-prices-master/data/wti-year')
new_format(population_df, '../data/population-master/data/population')
new_format(ppp_df, '../data/ppp-master/data/ppp-gdp')
