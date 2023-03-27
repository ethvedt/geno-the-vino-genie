# Vino Geno
--------------------------------------------------------------------------------------------------------------------------------------------------------
########################################################################################################################################################
--------------------------------------------------------------------------------------------------------------------------------------------------------
## Description

Welcome to our CLI app, hosted by Geno the Vino Genie, who pairs your meal with one of several variaties of wine that we think would go best. 
Users should:
    be prompted with questions about their meal to narrow the wine specification.
    Should be given a type of wine, with an option to be given another type of wine.

--------------------------------------------------------------------------------------------------------------------------------------------------------
## Database Schema

We would have three databases:
    - meals.py - Contains meals and associated information, including general ingredient categories (e.g., meat type)
      - meat base
      - vegetable base
      - grain base
      - fruits?
      - region
      - flavor profile
    - wines.py = Contains wines and associated information, including category information( e.g., red/white, region)
      - grape varietal
      - region
      - year? (probably not)
    - meal_wine.py = Join table associating meals with wines in a many-to-many relationship

