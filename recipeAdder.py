import pandas as pd

recipeList = {}

while True:
    print('Enter the name of the recipe in lower case')
    print("Or enter 'Done' to finish")
    recipeName = input().lower()
    if recipeName == 'done':
        break
    else:
        recipeList[recipeName] = {}
    while True:
        print("Enter ingredient or enter 'Done' to finish")
        ingredient = input().lower()
        if ingredient == 'Done' or ingredient == 'done':
            break
        else:
            print('Enter quantity of ' + ingredient)
            ingredientQuantity = int(input())
            recipeList[recipeName][ingredient] = ingredientQuantity
            print(recipeList)

print(recipeList)

(pd.DataFrame.from_dict(data=recipeList, orient='index')
   .to_csv('recipeList.csv', header=False))


