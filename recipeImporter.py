import csv
import pandas as pd
import pprint

recipeList = {}
with open("recipes.csv", 'r') as data_file:
    data = csv.DictReader(data_file, delimiter=",")
    for row in data:
        item = recipeList.get(row["Recipe"], dict())
        item[row["Ingredient"]] = int(row["Quantity"])
        recipeList[row["Recipe"]] = item

pprint.pprint(recipeList)

# (pd.DataFrame.from_dict(data=recipeList, orient='index')
#    .to_csv('recipeList.csv', header=False))
