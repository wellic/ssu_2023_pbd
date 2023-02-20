import zipfile
import pandas as pd


# Get the necessary data from the archives and store it in ../data/
oil_prices_wti_zip = zipfile.ZipFile('../task/datasets/oil-prices.zip')
population_zip = zipfile.ZipFile('../task/datasets/population.zip')
ppp_zip = zipfile.ZipFile('../task/datasets/ppp.zip')

oil_prices_wti_zip.extract('oil-prices-master/data/brent-year.csv', '../data/')
oil_prices_wti_zip.extract('oil-prices-master/data/wti-year.csv', '../data/')
oil_prices_wti_zip.close()

population_zip.extract('population-master/data/population.csv', '../data/')
population_zip.close()

ppp_zip.extract('ppp-master/data/ppp-gdp.csv', '../data/')
ppp_zip.close()


def save_new_format(data, path, name):
    # Save data in 3 formats (CSV, EXCEL, JSON)
    data.to_csv(path + f'/{name}.csv', index=False)
    data.to_excel(path + f'/{name}.xlsx', index=False)
    data.to_json(path + f'/{name}.json', orient='table', index=False)


# Paths to received data
oil_prices_wti_path = '../data/oil-prices-master/data/'
population_path = '../data/population-master/data/'
ppp_path = '../data/ppp-master/data/'


# Read the data
oil_prices_df = pd.read_csv(oil_prices_wti_path + '/brent-year.csv')
wti_year_df = pd.read_csv(oil_prices_wti_path + '/wti-year.csv')
population_df = pd.read_csv(population_path + 'population.csv')
ppp_df = pd.read_csv(ppp_path + 'ppp-gdp.csv')


# Change and adjust the date format for oil prices and wti
oil_prices_df['Date'] = pd.to_datetime(oil_prices_df.Date)
oil_prices_df['Date'] = oil_prices_df['Date'].dt.strftime('%Y')
wti_year_df['Date'] = pd.to_datetime(wti_year_df.Date)
wti_year_df['Date'] = wti_year_df['Date'].dt.strftime('%Y')


# Leave only the cities according to my variant in the dataframes
countries = ['Cyprus', 'Equatorial Guinea', 'Ethiopia']
population_df = population_df[population_df['Country Name'].isin(countries)]
ppp_df = ppp_df[ppp_df['Country'].isin(countries)]


# Change and adjust the date format for modified population and ppp dataframes
population_df['Year'] = pd.to_datetime(population_df.Year, format='%Y')
population_df['Year'] = population_df['Year'].dt.strftime('%Y')
ppp_df['Year'] = pd.to_datetime(ppp_df.Year, format='%Y')
ppp_df['Year'] = ppp_df['Year'].dt.strftime('%Y')


# Save data in 3 formats
save_new_format(oil_prices_df, oil_prices_wti_path, 'brent-year')
save_new_format(wti_year_df, oil_prices_wti_path, 'wti-year')
save_new_format(population_df, population_path, 'population')
save_new_format(ppp_df, ppp_path, 'ppp-gdp')
