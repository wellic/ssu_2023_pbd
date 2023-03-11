# Пояснювальна записка та висновок до лабораторного практикуму

Результатом лабораторного практикуму для 3 країн

1. Білорусь
2. Гондурас
3. Кюрасао

є наступні матеріали.

## Кодова база

### Python code

- [extract_from_archive](src/extract_from_archive.py)

### Jupiter Notebooks

- [data_visualization](src/data_visualization.ipynb)


### Файли

#### Вхідні дані (разархівовані, сконвертовані та одразу сгенеровані дані)

##### Oil prices (year)

- CSV: [brent-year](data/oil-prices-master/data/brent-year.csv)
- JSON: [brent-year](data/oil-prices-master/data/brent-year.json)
- XLSX [brent-year](data/oil-prices-master/data/brent-year.xlsx)

##### wti (year)

- CSV: [wti-year](data/oil-prices-master/data/wti-year.csv)
- JSON: [wti-year](data/oil-prices-master/data/wti-year.json)
- XLSX [wti-year](data/oil-prices-master/data/wti-year.xlsx)

##### Population

- CSV: [population](data/population-master/data/population.csv)
- JSON: [population](data/population-master/data/population.json)
- XLSX [population](data/population-master/data/population.xlsx)

##### Purchasing power parities

- CSV: [ppp](data/ppp-master/data/ppp-gdp.csv)
- JSON: [ppp](data/ppp-master/data/ppp-gdp.json)
- XLSX [ppp](data/ppp-master/data/ppp-gdp.xlsx)


---

## Інструкція до роботи

1. Запускаемо [extract_from_archive](src/extract_from_archive.py).
2. Результат программи 1:
    1. дістаємо дані з архіву;
    2. Зчитуємо дані;
    3. Змінюємо формат дати;
    4. Зберігаємо дані в 3-х форматах (CSV, JSON, XLSX)
3. Виконуємо код програми 2 в ноутбук [data_visualization](src/data_visualization.ipynb).
4. Результат программи 2
    1. Популяція за 1960-2018 роки: [лінійний графік](img/population_line.png), [стовпчаста діаграма](img/population_bar.png), [секторна діаграма](img/population_pie.png).
    2. Основні стаститичні величини в табличному вигляді: [Білорусь](img/main_stat_values_belarus.png), [Гондурас](img/main_stat_values_honduras.png), [Кюрасао](img/main_stat_values_curacao.png).
    3. Зв'язок ціни на нафту з ppp: [графік](img/ppp_oil_price.png)
    4. Зв'язок популяції та ppp: [графік](img/population_ppp.png)
    5. Зв'язок популяції та цін на нафту: [графік](img/population_oil_price.png)
    6. Відсоток ppp окремої країни до серднього ppp всіх країн за рік: [графік](img/percentage_of_ppp.png)
       
