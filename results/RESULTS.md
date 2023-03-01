# Пояснювальна записка та висновок до лабораторного практикуму

Результатом лабораторного практикуму для 3 країн

1. Малайзія
2. Польща
3. Руанда

є наступні матеріали.

## Кодова база

### Python code

- [main](src/main.py)

### Jupiter Notebooks

- [main_graphs](src/main_graphs.ipynb)

### Файли

#### Вхідні дані (разархівовані та сконвертовані дані)

##### Oil Prices

- CSV: [brent-year](data/oil-prices-master/data/brent-year.csv)
- JSON: [brent-year](data/oil-prices-master/data/brent-year.json)
- XLSX [brent-year](data/oil-prices-master/data/brent-year.xlsx)

##### West Texas Intermediate Prices 

- CSV: [wti-year](data/oil-prices-master/data/wti-year.csv)
- JSON: [wti-year](data/oil-prices-master/data/wti-year.json)
- XLSX [wti-year](data/oil-prices-master/data/wti-year.xlsx)

##### Population 

- CSV: [population](data/population-master/data/population.csv)
- JSON: [population](data/population-master/data/population.json)
- XLSX [population](data/population-master/data/population.xlsx)

##### Purchasing Power Parity

- CSV: [ppp-gdp](data/ppp-master/data/ppp-gdp.csv)
- JSON: [ppp-gdp](data/ppp-master/data/ppp-gdp.json)
- XLSX [ppp-gdp](data/ppp-master/data/ppp-gdp.xlsx)

---

## Інструкція до роботи

1. Запускаємо [main](src/main.py).
2. Результати программи 1:
    1. Отримано розархівовані дані.
    2. Змінено формат дати даних.
    3. Збережено в 3-х форматах.
3. Виконуємо код програми 2 в ноутбук [main_graphs](src/main_graphs.ipynb)
4. Результати программи 2:
    1. Населення в 3-х країнах за період 1960-2018рр:
       [лінійний графік](img/population_in_countries1.png),
       [стовпчаста гістограма](img/population_in_countries2.png),
       [секторна діаграма](img/population_in_countries3.png).
    2. Основні статистичні величини по кожній країні (count, min, max, mean, std, квантіли 25%, 50%, 75%, 95%):
       [Малайзія](img/population_of_Malaysia_static.png),
       [Польща](img/population_of_Poland_static.png),
       [Руанда](img/population_of_Rwanda_static.png).
    3. Зв'язок ціни на паливо (oil prices) з паритетом купівельної здатності
       [лінійний графік](img/connection_oil_prices_ppp.png).
    4. Зв'язок ціни на паливо (wti) з паритетом купівельної здатності
       [лінійний графік](img/connection_wti_ppp.png).
    5. Зв'язок між населенням країн та паритетом купівельної здатності
       [лінійний графік](img/connection_population_ppp.png).
    6. Зв'язок між налесенням та ціною на паливо (oil prices)
       [лінійний графік](img/cconnection_oil_population.png).
    7. Відсоток паритету купільвельної здатності (ppp) окремої країни до серднього паритету (ppp) всіх країн за кожен рік
       [лінійний графік](img/perc_ppp_country.png).
