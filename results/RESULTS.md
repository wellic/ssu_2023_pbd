# Пояснювальна записка та висновок до лабораторного практикуму

Результатом лабораторного практикуму для 3 країн

1. Кіпр
2. Екваторіальна Ґвінея
3. Ефіопія

є наступні матеріали.

## Кодова база

### Python code

- [data extraction](src/data_extraction.py)

### Jupiter Notebooks

- [display of graphs](src/display_of_graphs.ipynb)

### Файли

#### Вхідні дані (разархівовані та сконвертовані дані)

##### Oil prices

- CSV: [brent-year](data/oil_prices/brent-year.csv)
- JSON: [brent-year](data/oil_prices/brent-year.json)
- XLSX: [brent-year](data/oil_prices/brent-year.xlsx)

##### Population

- CSV: [population](data/population/population.csv)
- JSON: [population](data/population/population.json)
- XLSX: [population](data/population/population.xlsx)

##### PPP

- CSV: [ppp-gdp](data/ppp/ppp-gdp.csv)
- JSON: [ppp-gdp](data/ppp/ppp-gdp.json)
- XLSX: [ppp-gdp](data/ppp/ppp-gdp.xlsx)

##### WTI prices

- CSV: [wti-year](data/wti/wti-year.csv)
- JSON: [wti-year](data/wti/wti-year.json)
- XLSX: [wti-year](data/wti/wti-year.xlsx)

#### Сгенеровані нові дані

##### Population

- CSV: [Population](data/population/population_by_variant.csv)
- JSON: [Population](data/population/population_by_variant.json)
- XLSX: [Population](data/population/population_by_variant.xlsx)

##### PPP

- CSV: [ppp-gdp](data/ppp/ppp-gdp_by_variant.csv)
- JSON: [ppp-gdp](data/ppp/ppp-gdp_by_variant.json)
- XLSX: [ppp-gdp](data/ppp/ppp-gdp_by_variant.xlsx)

---

## Інструкція до роботи

1. Запускаемо [data extraction](src/data_extraction.py).
2. Результат программи 1:
    1. Отримано необхідні дані з архіву та збережено їх у ../data/.
    2. Змінено і налаштовано формат дати для всіх датасетів.
    3. Збережено дані в трьох форматах (CSV, XLSX, JSON).
    4. Для датасетів population та ppp збережено дані країн згідно варіанту.
    5. Збережено згенеровані дані в трьох форматах (CSV, XLSX, JSON).
    6. Видалено непотрібні директорії.
3. Виконуємо код програми 2 в ноутбук [display of graphs](src/display_of_graphs.ipynb).
4. Результат программи 2
    1. Популяція за країнами за інтервал часу 1960-2018 роки:
       [лінійний графік](img/population_in_countries_line.png), 
       [кругова діаграма](img/population_in_countries_pie.png), 
       [стовпчаста гістограма](img/population_in_countries_bar.png).
    2. Основні статистичні величини популяції за країнами:
       [Кіпр](img/main_statistical_values_cyprus.png), 
       [Екваторіальна Ґвінея](img/main_statistical_values_equatorial_guinea.png), 
       [Ефіопія](img/main_statistical_values_ethiopia.png),
    3. Зв'язок ціни на нафту з ррр по рокам по кожній країні варіанту:
       [Коефіцієнт кореляції по Кіпру](img/heatmap_oil_ppp_cyprus.png), 
       [Зв'язок по Кіпру](img/correlation_oil_and_ppp_cyprus.png),
       [Коефіцієнт кореляції по Екваторіальній Ґвінеї](img/heatmap_oil_ppp_guinea.png), 
       [Зв'язок по Екваторіальній Ґвінеї](img/correlation_oil_and_ppp_guinea.png),
       [Коефіцієнт кореляції по Ефіопії](img/heatmap_oil_ppp_ethiopia.png), 
       [Зв'язок по Ефіопії](img/correlation_oil_and_ppp_ethiopia.png).
   4. Зв'язок популяції та ррр по рокам по кожній країні варіанту:
       [Коефіцієнт кореляції по Кіпру](img/heatmap_population_ppp_cyprus.png), 
       [Зв'язок по Кіпру](img/correlation_population_and_ppp_cyprus.png),
       [Коефіцієнт кореляції по Екваторіальній Ґвінеї](img/heatmap_population_ppp_guinea.png), 
       [Зв'язок по Екваторіальній Ґвінеї](img/correlation_population_and_ppp_guinea.png),
       [Коефіцієнт кореляції по Ефіопії](img/heatmap_population_ppp_ethiopia.png), 
       [Зв'язок по Ефіопії](img/correlation_population_and_ppp_ethiopia.png).
   5. Зв'язок популяції та ціни на нафту по кожній країні варіанту:
       [Коефіцієнт кореляції по Кіпру](img/heatmap_population_oil_cyprus.png), 
       [Зв'язок по Кіпру](img/correlation_population_and_oil_cyprus.png),
       [Коефіцієнт кореляції по Екваторіальній Ґвінеї](img/heatmap_population_oil_guinea.png), 
       [Зв'язок по Екваторіальній Ґвінеї](img/correlation_population_and_oil_guinea.png),
       [Коефіцієнт кореляції по Ефіопії](img/heatmap_population_oil_ethiopia.png), 
       [Зв'язок по Ефіопії](img/correlation_population_and_oil_ethiopia.png).
   6. Відсоток ррр окремої країни до середнього рр всіх країн: 
       [Лінійний графік](img/percentage_ppp.png)