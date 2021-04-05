import pprint
import pandas as pd
import xlsxwriter

recipes = {'blackened chicken': {'allspice': 1,
                       'avocado': 1,
                       'chicken breast': 2,
                       'coriander': 1,
                       'lime': 2,
                       'mango': 1,
                       'mint': 1,
                       'quinoa 300g': 1,
                       'red capsicum': 1,
                       'red chilli': 1,
                       'smoked paprika': 1,
                       'spinach': 100,
                       'spring onion': 4,
                       'yellow capsicum': 1},
 'cajun chicken': {'cajun': 1,
                   'chicken breast': 2,
                   'coriander leaves': 1,
                   'corn': 4,
                   'lime': 2,
                   'polenta': 1,
                   'red chilli': 1,
                   'spring onion': 4,
                   'sweet potato 800g': 1,
                   'tomato': 3},
 'chicken fajitas': {'avocado': 1,
                     'chicken breast': 1,
                     'coriander leaves': 1,
                     'eggplant': 1,
                     'flour': 250,
                     'green capsicum': 1,
                     'lime': 2,
                     'oregano': 1,
                     'red capsicum': 1,
                     'red onion': 1,
                     'red wine vinegar': 1,
                     'smoked paprika': 1,
                     'tabasco': 1,
                     'yellow capsicum': 1},
 'chicken goujons': {'avocado': 1,
                     'baby cos 2pk': 1,
                     'basil fresh': 1,
                     'cherry tomato': 1,
                     'chicken breast': 2,
                     'egg': 1,
                     'flour': 250,
                     'lemon': 1},
 'daal curry': {'brown onion': 1,
                'cherry tomato': 2,
                'chilli powder': 1,
                'coriander': 1,
                'curry leaves': 1,
                'flour': 250,
                'ginger': 1,
                'lemon': 2,
                'light coconut milk 400g': 1,
                'mustard seeds': 1,
                'red capsicum': 1,
                'red chilli': 1,
                'red split lentils 300g': 1,
                'spinach': 200,
                'tumeric': 1},
 'falafel': {'baking soda': 1,
             'cardamom': 1,
             'chickpea flour': 1,
             'continental parsley': 1,
             'coriander': 1,
             'cucumber': 1,
             'cumin': 1,
             'dried chickpeas 1cup': 1,
             'flour': 250,
             'green chilli': 1,
             'hummus': 1,
             'lemon': 1,
             'red onion': 1,
             'spinach': 120,
             'tomato': 2},
 'greek chicken': {'allspice': 1,
                   'chicken breast': 2,
                   'couscous 150g': 1,
                   'cucumber': 1,
                   'dill': 1,
                   'frozen peas': 200,
                   'lemon': 1,
                   'mint': 1,
                   'oregano': 1,
                   'red capsicum': 1,
                   'red chilli': 1,
                   'spring onion': 4,
                   'yellow capsicum': 1},
 'happy cow burger': {'broad beans 200g': 1,
                      'burger buns': 1,
                      'carrot': 4,
                      'cayenne': 1,
                      'cheese': 1,
                      'coriander': 1,
                      'cumin': 1,
                      'gherkins': 4,
                      'green appple': 1,
                      'ground coriander': 1,
                      'lemon': 1,
                      'mixed beans': 1,
                      'mustard': 1,
                      'red onion': 1,
                      'savoy quarter': 1,
                      'tomato': 2,
                      'white wine vinegar': 1},
 'leek and potato soup': {'brown onion': 4,
                          'carrot': 4,
                          'celery': 4,
                          'leek': 4,
                          'stock': 1,
                          'white potato 800g': 1},
 'okonomiyaki': {'brown onion': 1,
                 'button mushrooms 100g': 1,
                 'chilli flakes': 1,
                 'cucumber': 1,
                 'egg': 6,
                 'flour': 150,
                 'radishes': 1,
                 'silken tofu 350g': 1,
                 'tamari': 1,
                 'white wine vinegar': 1,
                 'wombok half': 1},
 'ratatouille': {'balsamic vinegar': 1,
                 'chilli powder': 1,
                 'cumin': 1,
                 'eggplant': 1,
                 'ground coriander': 1,
                 'passata 700g': 1,
                 'red capsicum': 1,
                 'red onion': 1,
                 'rice': 1,
                 'smoked paprika': 1,
                 'yellow capsicum': 1,
                 'zucchini': 1},
 'salmon and prawn fishcakes': {'cajun': 1,
                                'cucumber': 1,
                                'dill': 1,
                                'iceberg letuce': 1,
                                'lemon': 2,
                                'peeled cooked prawns 200g': 1,
                                'red chili': 1,
                                'red wine vinegar': 1,
                                'salmon 250g': 1,
                                'tomato': 4,
                                'white potato 500g': 1},
 'salmon tacos': {'avocado': 2,
                  'cholula': 1,
                  'cucumber': 1,
                  'flour': 250,
                  'lime': 2,
                  'mint': 1,
                  'red onion': 1,
                  'salmon 500g': 1,
                  'white wine vinegar': 1},
 'salmon tray bake': {'broccoli': 1,
                      'cucumber': 1,
                      'ginger': 1,
                      'lime': 3,
                      'mango': 1,
                      'mint': 1,
                      'red chilli': 1,
                      'rice': 1,
                      'salmon 500g': 1,
                      'sesame seeds': 1,
                      'spring onion': 4,
                      'tamari': 1,
                      'white wine vinegar': 1},
 'sticky chicken noodles': {'black beans': 1,
                            'brown onion': 1,
                            'brown rice noodles': 1,
                            'carrot': 1,
                            'chicken breast': 2,
                            'cornflour': 1,
                            'five spice': 1,
                            'lime': 1,
                            'maple syrup': 1,
                            'pineapple rings 227g': 1,
                            'red chilli': 1,
                            'tamari': 1,
                            'white wine vinegar': 1,
                            'wombok half': 1},
 'sweet and sour fish balls': {'carrot': 2,
                               'coriander': 1,
                               'cornflour': 1,
                               'egg': 1,
                               'five spice': 1,
                               'frozen peas': 75,
                               'ginger': 1,
                               'peeled raw prawns 250g': 1,
                               'pineapple chunks 227g': 1,
                               'red capsicum': 1,
                               'rice': 1,
                               'spring onion': 4,
                               'squid tubes 400g': 1,
                               'tabasco': 1,
                               'tamari': 1,
                               'tomato paste': 1,
                               'white wine vinegar': 1,
                               'yellow capsicum': 1},
 'sweet potato soup': {'brown onion': 4,
                       'butternut squash half': 2,
                       'carrot': 4,
                       'celery': 4,
                       'continental parsley': 1,
                       'curry powder': 1,
                       'red chilli': 2,
                       'stock': 1,
                       'sweet potato 800g': 1},
 'tray baked chicken': {'balsamic vinegar': 1,
                        'chicken breast': 2,
                        'red capsicum': 1,
                        'red onion': 2,
                        'smoked paprika': 1,
                        'thyme': 1,
                        'tomato': 4,
                        'yellow capsicum': 1},
 'trout al forno': {'brown onion': 1,
                    'butternut squash half': 2,
                    'lemon': 2,
                    'mustard': 1,
                    'red potato 800g': 1,
                    'rosemary': 1,
                    'salmon 500g': 1,
                    'spinach': 120,
                    'thyme': 1},
 'veg rosti': {'carrot': 3,
               'egg': 4,
               'frozen peas': 100,
               'lemon': 1,
               'mustard': 1,
               'red potato 600g': 1,
               'spinach': 100},
 'veggie chilli': {'avocado': 2,
                   'black beans': 1,
                   'cherry tomato': 1,
                   'chickpeas': 1,
                   'chipotle chilli': 1,
                   'coriander': 1,
                   'cos': 1,
                   'cucumber': 1,
                   'cumin seeds': 1,
                   'lime': 2,
                   'passata 700g': 1,
                   'red capsicum': 1,
                   'red chilli': 1,
                   'red onion': 1,
                   'rice': 1,
                   'smoked paprika': 1,
                   'yellow capsicum': 1},
 'veggie feijoada': {'bay leaves': 1,
                     'black beans': 2,
                     'butternut squash half': 1,
                     'coriander leaves': 1,
                     'green capsicum': 1,
                     'ground coriander': 1,
                     'lime': 1,
                     'red capsicum': 1,
                     'red chilli': 1,
                     'red onion': 2,
                     'rice': 1,
                     'smoked paprika': 1,
                     'tomato': 2,
                     'yellow capsicum': 1}}

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

meatDairyEggs = ['chicken breast', 'salmon 500g', 'salmon 250g', 'egg',
    'peeled cooked prawns 200g','peeled raw prawns 250g', 'squid tubes 400g',
    'cheese', 'silken tofu 350g', 'hummus', 'butter']
frozenStuff = ['broad beans 200g', 'frozen peas', 'frozen veg', 'frozen corn']
pantryStuff = ['mustard', 'flour','white wine vinegar',
    'cholula','maple syrup', 'pineapple rings 227g',
    'tamari', 'cornflour', 'brown rice noodles',
    'black beans', 'tomato paste', 'tabasco',
    'pineapple chunks 227g', 'red wine vinegar',
    'balsamic vinegar', 'polenta', 'quinoa 300g',
    'quinoa', 'passata 700g', 'rice', 'couscous 150g',
    'couscous', 'red split lentils 300g', 'red split lentils',
    'light coconut milk 400g', 'light coconut milk',
    'mixed beans', 'red kidney beans', 'chickpeas',
    'gherkins', 'stock', 'dried chickpeas 1cup',
    'chickpea flour', 'baking soda']
spiceStuff = ['cayenne', 'cajun', 'allspice',
    'mustard seeds', 'five spice', 'chilli flakes',
    'thyme', 'oregano','cumin', 'smoked paprika',
    'tumeric', 'chilli powder', 'ground coriander',
    'cumin seeds', 'sesame seeds', 'basil', 'rosemary',
    'bay leaves', 'curry powder', 'cardamom', 'cinnamon']

meatDairyEggsList = {'-': '-'}
frozenList = {'-': '-'}
pantryList = {'-': '-'}
spiceList = {'-': '-'}
produceList = {'-': '-'}

for k, v in finalList.items():
    if k in meatDairyEggs:
        if k in meatDairyEggsList.keys():
            meatDairyEggsList[k] = meatDairyEggsList[k] + v
        else:
            meatDairyEggsList[k] = v
    elif k in frozenStuff:
        if k in frozenList.keys():
            frozenList[k] = frozenList[k] + v
        else:
            frozenList[k] = v
    elif k in pantryStuff:
        if k in pantryList.keys():
            pantryList[k] = pantryList[k] + v
        else:
            pantryList[k] = v
    elif k in spiceStuff:
        if k in spiceList.keys():
            spiceList[k] = spiceList[k] + v
        else:
            spiceList[k] = v
    else:
        if k in produceList.keys():
            produceList[k] = produceList[k] + v
        else:
            produceList[k] = v


print(meatDairyEggsList)
print(frozenList)
print(pantryList)
print(spiceList)
print(produceList)

df1 = pd.DataFrame.from_dict(data=meatDairyEggsList, orient='index')
df2 = pd.DataFrame.from_dict(data=frozenList, orient='index')
df3 = pd.DataFrame.from_dict(data=pantryList, orient='index')
df4 = pd.DataFrame.from_dict(data=spiceList, orient='index')
df5 = pd.DataFrame.from_dict(data=produceList, orient='index')

# print('Recipes chosen:')
# pprint.pprint(shoppingList)

# print('Final shopping list:')
# pprint.pprint(finalList)

writer = pd.ExcelWriter('shopppingList.xlsx', engine='xlsxwriter')

df5.to_excel(writer, sheet_name='Sheet1', header=['Produce'])
df2.to_excel(writer, sheet_name='Sheet1', header=['Frozen'], startcol=3)
df3.to_excel(writer, sheet_name='Sheet1', header=['Spices'], startrow=(len(frozenList)+2), startcol =3)
df4.to_excel(writer, sheet_name='Sheet1', header=['Pantry'], startcol=6)
df1.to_excel(writer, sheet_name='Sheet1', header=['Meats, Eggs and Dairy'], startrow=(len(pantryList)+2), startcol=6)

writer.save()




