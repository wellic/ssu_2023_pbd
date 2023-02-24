import zipfile
import pandas as pd

## Отримати необхідні дані з архіву та зберегти їх
oil_wti_zip = zipfile.ZipFile('../task/datasets/oil-prices.zip')
population_zip = zipfile.ZipFile('../task/datasets/population.zip')
ppp_gdp_zip = zipfile.ZipFile('../task/datasets/ppp.zip')
oil_wti_zip.extract('oil-prices-master/data/brent-year.csv', '../data/')
oil_wti_zip.extract('oil-prices-master/data/wti-year.csv', '../data/')
oil_wti_zip.close()
population_zip.extract('population-master/data/population.csv', '../data/')
population_zip.close()
ppp_gdp_zip.extract('ppp-master/data/ppp-gdp.csv', '../data/')
ppp_gdp_zip.close()

# Шляхи до отриманих даних
oil_wti_path = '../data/oil-prices-master/data'
popul_path = '../data/population-master/data'
ppp_gdp_path = '../data/ppp-master/data'

#Функція для збереження дани у 3-х форматах (CSV, EXCEL, JSON)
def save_in_three_formats(df, path_of_file, name_of_file):
    df.to_csv(f'{path_of_file}/{name_of_file}.csv', index=False)
    df.to_excel(f'{path_of_file}/{name_of_file}.xlsx', index=False)
    df.to_json(f'{path_of_file}/{name_of_file}.json', orient='table', index=False)

# Зчитуємо дані
oil_prices = pd.read_csv(oil_wti_path + '/brent-year.csv')
wti_year = pd.read_csv(oil_wti_path + '/wti-year.csv')
population = pd.read_csv(popul_path + '/population.csv')
ppp_gdp = pd.read_csv(ppp_gdp_path + '/ppp-gdp.csv')

# Зберігаємо дані в 3-х форматах
save_in_three_formats(oil_prices, oil_wti_path, 'brent-year')
save_in_three_formats(wti_year, oil_wti_path, 'wti-year')
save_in_three_formats(population, popul_path, 'population')
save_in_three_formats(ppp_gdp, ppp_gdp_path, 'ppp-gdp')

# Змінюємо і налаштовуємо формат даних для всіх наборів
oil_prices['Date'] = pd.to_datetime(oil_prices.Date)
oil_prices['Date'] = oil_prices['Date'].dt.strftime('%Y')
wti_year['Date'] = pd.to_datetime(wti_year.Date)
wti_year['Date'] = wti_year['Date'].dt.strftime('%Y')
population['Year'] = pd.to_datetime(population.Year, format='%Y')
population['Year'] = population['Year'].dt.strftime('%Y')
ppp_gdp['Year'] = pd.to_datetime(ppp_gdp.Year, format='%Y')
ppp_gdp['Year'] = ppp_gdp['Year'].dt.strftime('%Y')

# Зберігаємо нові дані в 3-х форматах
save_in_three_formats(oil_prices, oil_wti_path, 'brent-year_new')
save_in_three_formats(wti_year, oil_wti_path, 'wti-year_new')
save_in_three_formats(population, popul_path, 'population_new')
save_in_three_formats(ppp_gdp, ppp_gdp_path, 'ppp-gdp_new')

