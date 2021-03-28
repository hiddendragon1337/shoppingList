recipeList = {}

while True:
    print('Enter the name of the recipe in lower case')
    print("Or enter 'Done' to finish")
    recipeName = input()
    if recipeName == 'Done':
        break
    else:
        recipeList[recipeName] = {}
    while True:
        print("Enter ingredient or enter 'Done' to finish")
        ingredient = input()
        if ingredient == 'Done':
            break
        else:
            print('Enter quantity of ' + ingredient)
            ingredientQuantity = input()
            recipeList[recipeName][ingredient] = ingredientQuantity

print(recipeList)


