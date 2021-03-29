import pprint
import pandas as pd

recipes = {
    "bryce1": {"tomato": 3, "red onion": 2, "passata": 1},
    "sehrish1": {"salmon": 1, "apples": 2, "red onion": 1},
    "bryce2": {"tomato": 1, "red capsicum": 1, "passata": 1},
}

shoppingList = {}
while True:
    print("Please enter the name of a recipe.")
    print("Enter 'Help' for the list of recipes.")
    print("Enter 'Done' to finish and produce the shopping list.")
    recipeName = input().lower()
    if recipeName in recipes.keys():
        shoppingList[recipeName] = recipes[recipeName]
    elif recipeName == "done":
        break
    elif recipeName == "help":
        pprint.pprint(list(recipes.keys()))
    else:
        print("That recipe does not exist. Please try again.")

finalList = {}
for k, v in shoppingList.items():
    for k1, v1, in v.items():
        if k1 in finalList.keys():
            finalList[k1] = finalList[k1] + v1
        else:
            finalList[k1] = v1


print('Recipes chosen:')
pprint.pprint(shoppingList)

print('Final shopping list:')
pprint.pprint(finalList)

(pd.DataFrame.from_dict(data=finalList, orient='index')
   .to_csv('dict_file.csv', header=False))


