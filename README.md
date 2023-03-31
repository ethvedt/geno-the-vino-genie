# Vino Geno
--------------------------------------------------------------------------------------------------------------------------------------------------------
## Description

Welcome to our CLI app, hosted by Geno the Vino Genie, who pairs your meal with one of several variaties of wine that we think would go best. 
Users should:
    be prompted with questions about their meal to narrow the wine specification.
    be given a type of wine, with an option to be given another type of wine.

--------------------------------------------------------------------------------------------------------------------------------------------------------
## Database Schema

- We have three databases:
  - meals.py - Contains meals and associated information, including general ingredient categories (e.g., meat type)
    - ID
    - name
    - meat
    - vegetables
    - flavor profile
    - starch
    - spice
    - dairy
  - wines.py = Contains wines and associated information, including category information( e.g., red/white, region)
    - name
    - region
    - type
  - meal_wine.py = Table associating meals with wines in a many-to-many relationship

## Attributions

* https://patorjk.com/software/taag/ for the ASCII name.
* https://media.winefolly.com/food-and-wine-poster.jpg for general wine pairing information.
* https://github.com/bndr/pipreqs for auto-generating requirements.txt.