# Data Atlas

## Cleaned
Directory contains all cleaned data. Data cleaning is reproducible, 
code can be found in sweetgreen module and raw data
can be found in raw data directory

## Raw
Contains raw data from three sources

## Sweetgreen supplier chalkboards
* raw/restaurant_menus/

Pictures were taken at restaurant and text was manually transcribed.
There are likely errors in transcription so only use the data 
for a rough gauge and not precise analysis

## Sweetgreen wordpress menus
* raw/raw_ingredients.json
* raw/raw_menu_items.json

Both these json files were generated from HTML files of sweetgreens
menus. They were *not* used in any of the exploratory analysis.

## Sweetgreen orders application
* raw/raw_resturaunts.json
* raw/raw_resturaunts_presidents_day.json
* raw/restaurant_menus/
* raw/restaurant_menus_presidents_day/  

These json files came directly from sweetgreens public apis with
no data processing.

## USA Map Shapefile
* shapefile/

Shapefile data for roads came from US census site
https://www.census.gov/geo/maps-data/data/tiger-line.htm

