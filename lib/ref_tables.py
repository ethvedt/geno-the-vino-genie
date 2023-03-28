meat_list = ["red meat", "poultry", "pork", "fish", "game", "none"]
veg_list = ["allium", "green leafy", "root", "nightshade", "fungi", "nuts or seeds", "beans", "none"]
flavor_list = ["sweet", "spicy", "acidic", "rich", "bitter", "salty"]
starch_list = ["white", "whole wheat", "sweet veg", "potato", "none"]
spice_list = ["black pepper", "red pepper", "hot and spicy", "herbs", "baking", "other"]
dairy_list = ["soft cheese or cream", "hard cheese", "pungent cheese", "none"]
wine_list = ["bold red", "medium red", "light red", "rose", "rich white", "light white", "sparkling", "sweet white", "dessert"]
meat_table = {
        "red meat": [2, 1, 0, 0, 0, 0, 0, 0, 0],
        "poultry": [0, 1, 2, 1, 2, 1, 1, 0, 0],
        "pork": [1, 2, 0, 1, 0, 0, 1, 0, 0],
        "fish": [0, 0, 0, 0, 1, 2, 1, 0, 0],
        "game": [2, 1, 0, 0, 0, 0, 0, 0, 0],
        "none": [0, 0, 0, 0, 0, 0, 0, 0, 0]
}

veg_table = {
        "allium": [1, 2, 1, 1, 1, 1, 1, 1, 0],
        "green leafy": [0, 0, 0, 0, 0, 2, 1, 0, 0],
        "root": [0, 0, 0, 2, 1, 0, 0, 1, 0],
        "nightshade": [1, 2, 0, 1, 0, 0, 0, 1, 0],
        "fungi": [1, 2, 2, 0, 2, 0, 0, 0, 0],
        "nuts or seeds": [0, 0, 1, 1, 1, 1, 1, 2, 0],
        "beans": [0, 1, 0, 1, 0, 2, 1, 0, 0],
        "none": [0, 0, 0, 0, 0, 0, 0, 0, 0]
}

flavor_table = {
        "sweet": [0, 0, 0, 1, 1, 0, 0, 1, 2],
        "spicy": [0, 0, 0, 0, 1, 0, 1, 2, 1],
        "acidic": [0, 0, 1, 0, 1, 2, 0, 0, 0],
        "rich": [2, 1, 1, 0, 0, 1, 1, 0, 0],
        "bitter": [0, 0, 0, 0, 2, 1, 1, 2, 1],
        "salty": [0, 0, 1, 1, 0, 2, 1, 0, 0]
    }

starch_table = {
        "white": [1, 1, 1, 1, 1, 1, 1, 1, 1], 
        "whole wheat": [0, 0, 1, 1, 1, 0, 0, 2, 0], 
        "sweet veg": [0, 0, 0, 1, 0, 0, 0, 2, 0], 
        "potato": [1, 1, 1, 1, 1, 1, 1, 1, 0],
        "none": [0, 0, 0, 0, 0, 0, 0, 0, 0]
}

spice_table = {
        "black pepper": [2, 1, 0, 0, 0, 0, 0, 0, 0], 
        "red pepper": [1, 2, 0, 1, 0, 0, 1, 1, 1], 
        "hot and spicy": [0, 0, 0, 0, 0, 1, 1, 2, 0], 
        "herbs": [0, 1, 1, 1, 1, 2, 0, 0, 0], 
        "baking": [0, 1, 0, 1, 0, 0, 0, 1, 2], 
        "other": [0, 0, 0, 0, 0, 0, 0, 0, 0]
}

dairy_table = {
        "cream": [0, 1, 2, 1, 2, 1, 1, 1, 1], 
        "soft cheese": [0, 1, 2, 1, 2, 1, 1, 1, 1], 
        "hard cheese": [2, 1, 0, 1, 1, 0, 1, 0, 0], 
        "pungent cheese": [1, 2, 0, 1, 0, 1, 1, 1, 2],
        "none": [0, 0, 0, 0, 0, 0, 0, 0, 0]
}

dispatch_table = {
            "meat": meat_table,
            "veg": veg_table,
            "flavor": flavor_table,
            "starch": starch_table,
            "spice": spice_table,
            "dairy": dairy_table
}