import pprint
import pandas as pd
import xlsxwriter
import fpdf
import sys
import collections

recipes = {'blackened chicken': {'allspice': 1,
                       'avocado': 1,
                       'chicken breast': 2,
                       'coriander': 1,
                       'lime': 2,
                       'mango': 1,
                       'mint': 1,
                       'quinoa 300g': 1,
                       'capsicum red': 1,
                       'red chilli': 1,
                       'smoked paprika': 1,
                       'spinach': 100,
                       'spring onion': 4,
                       'capsicum yellow': 1},
 'bryce': {'almonds': 1,
           'banana': 4,
           'cashews': 1,
           'frozen fruit bryce': 2,
           'milk bryce': 1,
           'raisin toast': 1,
           'tissues': 1,
           'walnuts': 1,
           'popcorn': 1,
           'wheat biscuits': 1,
           'yoghurt': 3},
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
 'cajun salmon and black bean salad': {'black beans': 3,
                                       'cajun': 1,
                                       'cherry tomato': 1,
                                       'chilli powder': 1,
                                       'coriander': 1,
                                       'cumin': 1,
                                       'frozen corn 1 cup': 1,
                                       'jalapeno': 1,
                                       'lemon': 1,
                                       'lime': 1,
                                       'olive oil': 1,
                                       'capsicum red': 1,
                                       'onion red': 1,
                                       'salmon 500g': 1,
                                       'salt': 1,
                                       'white wine vinegar': 1},
 'cajun salmon and quinoa salad': {'cajun': 1,
                                   'chickpeas': 1,
                                   'continental parsley': 1,
                                   'cucumber': 1,
                                   'garlic': 2,
                                   'lemon': 3,
                                   'olive oil': 1,
                                   'pepper': 1,
                                   'quinoa 1 cup': 1,
                                   'capsicum red': 1,
                                   'onion red': 1,
                                   'red wine vinegar': 1,
                                   'salmon 500g': 1,
                                   'salt': 1},
 'cajun salmon and roast pumpkin and rice salad': {'butternut squash half': 1,
                                                   'cajun': 1,
                                                   'frozen peas': 150,
                                                   'hazelnuts': 1,
                                                   'lemon': 1,
                                                   'maple syrup': 1,
                                                   'moroccan seasoning': 1,
                                                   'olive oil': 1,
                                                   'rice blend 1 cup': 1,
                                                   'salmon 500g': 1,
                                                   'snap peas': 150,
                                                   'white wine vinegar': 1},
 'cajun salmon and seedy slaw': {'cajun': 1,
                                 'carrot': 4,
                                 'continental parsley': 1,
                                 'cumin': 1,
                                 'garlic': 1,
                                 'green cabbage quarter': 1,
                                 'lemon': 3,
                                 'olive oil': 1,
                                 'pumpkin seeds': 1,
                                 'purple cabbage quarter': 1,
                                 'salmon 500g': 1,
                                 'salt': 1},
 'cashew chicken and veggie fried rice': {'onion brown': 1,
                                          'cashews unsalted': 1,
                                          'chicken breast': 2,
                                          'chilli flakes': 1,
                                          'cornstarch': 1,
                                          'date sugar': 1,
                                          'frozen veg': 1,
                                          'garlic': 3,
                                          'ginger': 1,
                                          'capsicum green': 1,
                                          'oilve oil': 1,
                                          'pepper': 1,
                                          'portabello mushrooms 1 cup': 1,
                                          'capsicum red': 1,
                                          'rice': 1,
                                          'salt': 1,
                                          'soy sauce': 1,
                                          'stock': 1,
                                          'tabasco': 1},
 'chicken fajitas': {'avocado': 1,
                     'chicken breast': 2,
                     'coriander leaves': 1,
                     'eggplant': 1,
                     'flour': 250,
                     'capsicum green': 1,
                     'lime': 2,
                     'oregano': 1,
                     'capsicum red': 1,
                     'onion red': 1,
                     'red wine vinegar': 1,
                     'smoked paprika': 1,
                     'tabasco': 1,
                     'capsicum yellow': 1},
 'chicken goujons': {'avocado': 1,
                     'baby cos 2pk': 1,
                     'basil': 1,
                     'cherry tomato': 1,
                     'chicken breast': 2,
                     'egg': 1,
                     'flour': 250,
                     'lemon': 1},
 'chicken jalfrezi': {'onion brown': 1,
                      'cayenne': 1,
                      'chicken breast': 2,
                      'jalfrezi curry paste': 1,
                      'lemon': 1,
                      'plum tomatoes 400g': 1,
                      'capsicum red': 2,
                      'onion red': 1,
                      'rice': 1,
                      'capsicum yellow': 1},
 'chicken pasta and herby veg ragu': {'balsamic vinegar': 1,
                                      'bay leaves': 1,
                                      'carrot': 1,
                                      'celery': 1,
                                      'chicken breast': 2,
                                      'fusilli': 200,
                                      'garlic': 4,
                                      'leek': 1,
                                      'olive oil': 1,
                                      'passata 700g': 1,
                                      'pine nuts': 1,
                                      'capsicum red': 1,
                                      'red chilli': 1,
                                      'rosemary': 1,
                                      'thyme': 1,
                                      'zucchini': 1},
 'chicken tikka masala': {'onion brown': 1,
                          'chicken breast': 1,
                          'chickpeas': 1,
                          'chilli flakes': 1,
                          'chopped tomatoes 800g': 1,
                          'cumin': 1,
                          'date sugar': 1,
                          'garam masala': 1,
                          'garlic': 6,
                          'ginger': 1,
                          'ground coriander': 1,
                          'jalapeno': 1,
                          'light coconut milk 400g': 1,
                          'olive oil': 1,
                          'capsicum red': 1,
                          'rice': 1,
                          'salt': 1,
                          'smoked paprika': 1,
                          'tumeric': 1},
 'chilli con carne': {'balsamic vinegar': 1,
                      'onion brown': 2,
                      'carrot': 2,
                      'celery': 2,
                      'chickpeas': 1,
                      'chilli powder': 1,
                      'chopped tomatoes 800g': 1,
                      'cinnamon': 1,
                      'coriander': 1,
                      'cumin': 1,
                      'garlic': 1,
                      'kidney beans': 1,
                      'lime': 1,
                      'olive oil': 1,
                      'pepper': 1,
                      'capsicum red': 2,
                      'rice': 1,
                      'salt': 1},
 'daal curry': {'onion brown': 1,
                'cherry tomato': 2,
                'chilli powder': 1,
                'coriander': 1,
                'curry leaves': 1,
                'flour': 250,
                'ginger': 1,
                'lemon': 2,
                'light coconut milk 400g': 1,
                'mustard seeds': 1,
                'capsicum red': 1,
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
             'onion red': 1,
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
                   'capsicum red': 1,
                   'red chilli': 1,
                   'spring onion': 4,
                   'capsicum yellow': 1},
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
                      'onion red': 1,
                      'savoy quarter': 1,
                      'tomato': 2,
                      'white wine vinegar': 1},
 'huevos rancheros': {'bread': 1,
                      'onion brown': 1,
                      'chopped tomatoes 400g': 1,
                      'chopped tomatoes 800g': 1,
                      'coriander': 1,
                      'cumin': 1,
                      'egg': 4,
                      'garlic': 2,
                      'jalapeno': 1,
                      'kidney beans': 1,
                      'olive oil': 1,
                      'capsicum red': 1},
 'jalrezi curry paste': {'coriander': 1,
                         'coriander seeds': 1,
                         'cumin seeds': 1,
                         'fenugreek seeds': 1,
                         'garlic': 2,
                         'ginger': 1,
                         'lemon': 1,
                         'mustard seeds': 1,
                         'olive oil': 1,
                         'red chilli': 1,
                         'salt': 1,
                         'tomato paste': 1,
                         'tumeric': 1},
 'leek and potato soup': {'onion brown': 4,
                          'carrot': 4,
                          'celery': 4,
                          'leek': 4,
                          'stock': 1,
                          'white potato 800g': 1},
 'lentil and chickpea burgers': {'avocado': 1,
                                 'onion brown': 1,
                                 'burger buns': 4,
                                 'canned lentils': 2,
                                 'carrot': 1,
                                 'chickpeas': 1,
                                 'chilli powder': 1,
                                 'coriander': 1,
                                 'cumin': 1,
                                 'egg': 2,
                                 'flour': 50,
                                 'garlic': 4,
                                 'gherkins': 1,
                                 'ground coriander': 1,
                                 'jalapeno': 2,
                                 'lemon': 1,
                                 'mint': 1,
                                 'oats 1/2 cup': 1,
                                 'olive oil': 1,
                                 'pepper': 1,
                                 'salt': 1,
                                 'smoked paprika': 1,
                                 'tabasco': 1,
                                 'tomato': 2},
 'lentil soup': {'bread': 1,
                 'onion brown': 2,
                 'carrot': 4,
                 'chilli flakes': 1,
                 'chopped tomatoes 800g': 2,
                 'cumin': 1,
                 'curry powder': 1,
                 'garlic': 8,
                 'green lentils 2 cups': 1,
                 'kale 2 cups': 1,
                 'lemon': 2,
                 'olive oil': 1,
                 'pepper': 1,
                 'salt': 1,
                 'stock': 1,
                 'thyme': 1},
 'okonomiyaki': {'onion brown': 1,
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
 'orange chicken and veggie fried rice': {'onion brown': 1,
                                          'chicken breast': 2,
                                          'cornstarch': 1,
                                          'date sugar': 1,
                                          'egg': 2,
                                          'frozen veg': 1,
                                          'garlic': 2,
                                          'ginger': 1,
                                          'olive oil': 1,
                                          'orange': 1,
                                          'portabello mushrooms 1 cup': 1,
                                          'capsicum red': 1,
                                          'rice': 1,
                                          'snap peas': 150,
                                          'soy sauce': 1,
                                          'tabasco': 1},
 'pea and mint soup': {'onion brown': 2,
                       'carrot': 2,
                       'celery': 2,
                       'frozen peas': 800,
                       'garlic': 1,
                       'mint': 1,
                       'olive oil': 1,
                       'pepper': 1,
                       'salt': 1,
                       'stock': 1},
 'pizza': {'basil dried': 1,
           'onion brown': 1,
           'chilli flakes': 1,
           'date sugar': 1,
           'flour': 480,
           'frozen corn 1 cup': 1,
           'garlic': 5,
           'mozerella': 1,
           'olive oil': 1,
           'oregano': 1,
           'pineapple half': 1,
           'plum tomatoes 400g': 1,
           'plum tomatoes 800g': 1,
           'portabello mushrooms 400-500g': 1,
           'capsicum red': 2,
           'salt': 1,
           'yeast': 1,
           'capsicum yellow': 1},
 'ratatouille': {'balsamic vinegar': 1,
                 'chilli powder': 1,
                 'cumin': 1,
                 'eggplant': 1,
                 'ground coriander': 1,
                 'passata 700g': 1,
                 'capsicum red': 1,
                 'onion red': 1,
                 'rice': 1,
                 'smoked paprika': 1,
                 'capsicum yellow': 1,
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
 'salmon patties': {'brocollini': 1,
                    'lemon': 1,
                    'parsley': 1,
                    'pepper': 1,
                    'polenta': 1,
                    'potato': 1,
                    'spring onion': 3,
                    'sweet potato': 1,
                    'tinned red salmon': 1},
 'salmon tacos': {'avocado': 2,
                  'cholula': 1,
                  'cucumber': 1,
                  'flour': 250,
                  'lime': 2,
                  'mint': 1,
                  'onion red': 1,
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
 'sehrish': {'almond butter': 1,
             'banana': 5,
             'bread': 1,
             'egg carton': 1,
             'frozen fruit sehrish': 2,
             'frozen veg': 1,
             'fruit': 7,
             'milk sehrish': 1,
             'seeds': 3,
             'weeties': 1,
             'yoghurt': 1},
 'sicilian stew': {'onion brown': 2,
                   'butternut squash half': 2,
                   'chickpeas': 1,
                   'chilli flakes': 1,
                   'chopped tomatoes 400g': 1,
                   'cinnamon': 1,
                   'coriander': 1,
                   'couscous 100g': 1,
                   'olive oil': 1,
                   'raisins 40g': 1,
                   'stock': 1},
 'smoky veggie chilli': {'almond butter': 1,
                         'bread': 1,
                         'onion brown': 2,
                         'butter beans': 2,
                         'cacao powder': 1,
                         'coriander': 1,
                         'cumin seeds': 1,
                         'capsicum green': 1,
                         'olive oil': 1,
                         'plum tomatoes 400g': 1,
                         'plum tomatoes 800g': 1,
                         'capsicum red': 1,
                         'red chilli': 2,
                         'smoked paprika': 1,
                         'sweet potato': 2,
                         'capsicum yellow': 1},
 'sticky chicken noodles': {'black beans': 1,
                            'onion brown': 1,
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
                               'capsicum red': 1,
                               'rice': 1,
                               'spring onion': 4,
                               'squid tubes 400g': 1,
                               'tabasco': 1,
                               'tamari': 1,
                               'tomato paste': 1,
                               'white wine vinegar': 1,
                               'capsicum yellow': 1},
 'sweet potato and chickpea curry': {'bread': 1,
                                     'cayenne': 1,
                                     'chickpeas': 1,
                                     'chopped tomatoes 800g': 1,
                                     'cinnamon': 1,
                                     'cumin': 1,
                                     'garlic': 2,
                                     'capsicum green': 1,
                                     'ground coriander': 1,
                                     'ground ginger': 1,
                                     'lemon': 1,
                                     'mustard seeds': 1,
                                     'red chilli': 1,
                                     'onion red': 1,
                                     'spinach': 60,
                                     'sweet potato': 2,
                                     'tumeric': 1},
 'sweet potato soup': {'onion brown': 4,
                       'butternut squash half': 2,
                       'carrot': 4,
                       'celery': 4,
                       'continental parsley': 1,
                       'curry powder': 1,
                       'red chilli': 2,
                       'stock': 1,
                       'sweet potato 800g': 1},
 'tex mex casserole': {'avocado': 2,
                       'black beans': 1,
                       'cayenne': 1,
                       'chilli powder': 1,
                       'chopped tomatoes 400g': 1,
                       'cumin': 1,
                       'frozen corn 1/2 cup': 1,
                       'garlic': 3,
                       'ground coriander': 1,
                       'olive oil': 1,
                       'paprika': 1,
                       'pepper': 1,
                       'capsicum red': 1,
                       'onion red': 1,
                       'rice': 1,
                       'salt': 1,
                       'spinach': 120,
                       'tomato paste 250ml': 1,
                       'capsicum yellow': 1},
 'tray baked chicken': {'balsamic vinegar': 1,
                        'chicken breast': 2,
                        'capsicum red': 1,
                        'onion red': 2,
                        'smoked paprika': 1,
                        'thyme': 1,
                        'tomato': 4,
                        'capsicum yellow': 1},
 'trout al forno': {'onion brown': 1,
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
 'vegan meatballs and pasta': {'balsamic vinegar': 1,
                               'basil fresh': 1,
                               'onion brown': 2,
                               'carrot': 1,
                               'celery': 1,
                               'chopped tomatoes 800g': 1,
                               'flax meal': 1,
                               'garlic': 1,
                               'italian seasoning': 1,
                               'oats 1/4 cup': 1,
                               'olive oil': 1,
                               'pecan 1/2 cup': 1,
                               'pepper': 1,
                               'portabello mushrooms 1 cup': 1,
                               'red chilli': 1,
                               'salt': 1,
                               'spaghetti': 250,
                               'tamari': 1,
                               'thyme': 1},
 'vegeree': {'baby spinach': 200,
             'cherry tomato': 1,
             'coriander': 1,
             'curry powder': 1,
             'egg': 4,
             'frozen peas': 200,
             'ginger': 1,
             'lemon': 2,
             'olive oil': 1,
             'portabello mushrooms': 3,
             'red chilli': 2,
             'rice': 1,
             'spring onion': 4},
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
                   'capsicum red': 1,
                   'red chilli': 1,
                   'onion red': 1,
                   'rice': 1,
                   'smoked paprika': 1,
                   'capsicum yellow': 1},
 'veggie feijoada': {'bay leaves': 1,
                     'black beans': 2,
                     'butternut squash half': 1,
                     'coriander leaves': 1,
                     'capsicum green': 1,
                     'ground coriander': 1,
                     'lime': 1,
                     'capsicum red': 1,
                     'red chilli': 1,
                     'onion red': 2,
                     'rice': 1,
                     'smoked paprika': 1,
                     'tomato': 2,
                     'capsicum yellow': 1},
 'vietnamese salmon salad': {'apples PL': 2,
                             'baby cos 2pk': 1,
                             'bread': 200,
                             'cucumber': 1,
                             'ginger': 1,
                             'green beans': 200,
                             'olive oil': 1,
                             'radishes': 1,
                             'red chilli': 1,
                             'salmon 500g': 1,
                             'soy sauce': 1,
                             'white wine vinegar': 1},
'blackened salmon and southwestern quinoa salad': {'black beans': 1,
                                                    'cayenne': 1,
                                                    'chilli powder': 1,
                                                    'frozen corn 1 cup': 1,
                                                    'garlic powder': 1,
                                                    'lemon': 1,
                                                    'lime': 1,
                                                    'mango': 1,
                                                    'maple syrup': 1,
                                                    'olive oil': 1,
                                                    'onion powder': 1,
                                                    'oregano': 1,
                                                    'paprika': 1,
                                                    'pepper': 1,
                                                    'red capsicum': 1,
                                                    'onion red': 1,
                                                    'red quinoa 1 cup': 1,
                                                    'salmon 500g': 1,
                                                    'salt': 1},
 'shrimp fajitas': {'prawns': 500,
                    'brown onion': 1,
                    'red capsicum': 1,
                    'yellow capsicum': 1,
                    'lime': 1,
                    'chilli powder': 1,
                    'cumin': 1,
                    'garlic powder': 1,
                    'paprika': 1,
                    'oregano': 1,
                    'avocado': 1,
                    'flour': 300},
 'enchilada sauce double': {'flour': 1,
                            'chilli powder': 2,
                            'cumin': 2,
                            'garlic powder': 1,
                            'oregano': 1,
                            'cinnamon': 1,
                            'tomato paste': 2,
                            'stock': 4,
                            'apple cider vinegar': 1},
 'enchilada': {'enchilada sauce': 1,
               'onion red': 1,
               'capsicum red': 1,
               'broccoli': 1,
               'cumin': 1,
               'cinnamon': 1,
               'baby spinach': 120,
               'black beans': 1,
               'flour': 300},
 'pan prawns': {'prawns': 600,
                'asparagus': 2,
                'corn': 4,
                'shallots': 6,
                'garlic': 2,
                'lemon': 2,
                'garlic powder': 1,
                'onion powder': 1,
                'smoked paprika': 1}}


shoppingList = {}
print("Enter 'Help' for the list of recipes.")
print("Enter 'Done' to finish and produce the shopping list.")
while True:
    print("Please enter the name of a recipe.")
    recipeName = input().lower()
    if recipeName in recipes.keys():
        shoppingList[recipeName] = recipes[recipeName]
    elif recipeName == "done":
        break
    elif recipeName == "help":
        pprint.pprint(list(recipes.keys()))
    else:
        print("ERROR! YOU ENTERED AN INVALID RECIPE. Please try again.")

finalList = {}
for k, v in shoppingList.items():
    for (
        k1,
        v1,
    ) in v.items():
        if k1 in finalList.keys():
            finalList[k1] = finalList[k1] + v1
        else:
            finalList[k1] = v1

meatDairyEggs = [
    "chicken breast",
    "salmon 500g",
    "salmon 250g",
    "egg",
    "egg carton",
    "prawns",
    "peeled cooked prawns 200g",
    "peeled raw prawns 250g",
    "squid tubes 400g",
    "cheese",
    "silken tofu 350g",
    "hummus",
    "butter",
    "milk bryce",
    "yoghurt",
    "eggs",
    "mozerella",
    "milk sehrish",
]
frozenStuff = [
    "broad beans 200g",
    "frozen peas",
    "frozen veg",
    "frozen corn",
    "frozen corn 1 cup",
    "frozen corn 1/2 cup",
    "frozen fruit bryce",
    "frozen fruit sehrish",
    "tissues",
]

pantryStuff = [
    "raisin toast",
    "wheat biscuits",
    "mustard",
    "red quinoa 1 cup",
    "flour",
    "white wine vinegar",
    "cholula",
    "maple syrup",
    "pineapple rings 227g",
    "tamari",
    "cornflour",
    "brown rice noodles",
    "black beans",
    "tomato paste",
    "tabasco",
    "pineapple chunks 227g",
    "red wine vinegar",
    "balsamic vinegar",
    "polenta",
    "popcorn",
    "quinoa 300g",
    "quinoa",
    "passata 700g",
    "rice",
    "couscous 150g",
    "couscous",
    "red split lentils 300g",
    "red split lentils",
    "light coconut milk 400g",
    "light coconut milk",
    "mixed beans",
    "red kidney beans",
    "chickpeas",
    "gherkins",
    "stock",
    "dried chickpeas 1cup",
    "chickpea flour",
    "baking soda",
    "almond butter",
    "weeties",
    "olive oil",
    "soy sauce",
    "date sugar",
    "tinned red salmon",
    "yeast",
    "plum tomatoes 800g",
    "plum tomatoes 400g",
    "cornstarch",
    "canned lentils",
    "oats 1/2 cup",
    "quinoa 1 cup",
    "chopped tomatoes 800g",
    "chopped tomatoes 400g",
    "kidney beans",
    "rice blend 1 cup",
    "green lentils 2 cups",
    "fusilli",
    "pine nuts",
    "jalfrezi curry paste",
    "tomato paste",
    "tomato paste 250ml",
    "cacao powder",
    "butter beans",
    "spaghetti",
    "flax meal"
    "oats 1/4 cup",
    "flax meal"
]

spiceStuff = [
    "cayenne",
    "cajun",
    "allspice",
    "mustard seeds",
    "five spice",
    "chilli flakes",
    "thyme",
    "oregano",
    "cumin",
    "smoked paprika",
    "tumeric",
    "chilli powder",
    "ground coriander",
    "cumin seeds",
    "coriander seeds",
    "fenugreek seeds",
    "sesame seeds",
    "basil dried",
    "rosemary",
    "bay leaves",
    "curry powder",
    "cardamom",
    "cinnamon",
    "paprika",
    "garlic powder",
    "onion powder",
    "salt",
    "pepper",
    "garam masala",
    "ground ginger",
    "moroccan seasoning",
    "italian seasoning"
]

nutStuff = [
    "almonds",
    "walnuts",
    "cashews",
    "seeds",
    "pumpkin seeds",
    "hazelnuts",
    "pecan 1/2 cup",
]

breadStuff = [
    "bread",
    "burger buns",
]

meatDairyEggsList = {}
frozenList = {}
pantryList = {}
spiceList = {}
produceList = {}
nutList = {}
breadList = {}

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
    elif k in nutStuff:
        if k in nutList.keys():
            nutList[k] = nutList[k] + v
        else:
            nutList[k] = v
    elif k in breadStuff:
        if k in breadList.keys():
            breadList[k] = breadList[k] + v
        else:
            breadList[k] = v
    else:
        if k in produceList.keys():
            produceList[k] = produceList[k] + v
        else:
            produceList[k] = v

if meatDairyEggsList == {}:
    meatDairyEggsList["-"] = "-"
if frozenList == {}:
    frozenList["-"] = "-"
if pantryList == {}:
    pantryList["-"] = "-"
if spiceList == {}:
    spiceList["-"] = "-"
if produceList == {}:
    produceList["-"] = "-"
if nutList == {}:
    nutList["-"] = "-"
if breadList == {}:
    breadList["-"] = "-"

print("Recipes chosen:")
pprint.pprint(shoppingList)

meatOD = collections.OrderedDict(sorted(meatDairyEggsList.items()))
frozenOD = collections.OrderedDict(sorted(frozenList.items()))
pantryOD = collections.OrderedDict(sorted(pantryList.items()))
spiceOD = collections.OrderedDict(sorted(spiceList.items()))
produceOD = collections.OrderedDict(sorted(produceList.items()))
nutOD = collections.OrderedDict(sorted(nutList.items()))
breadOD = collections.OrderedDict(sorted(breadList.items()))

df1 = pd.DataFrame.from_dict(data=meatOD, orient="index")
df2 = pd.DataFrame.from_dict(data=frozenOD, orient="index")
df3 = pd.DataFrame.from_dict(data=pantryOD, orient="index")
df4 = pd.DataFrame.from_dict(data=spiceOD, orient="index")
df5 = pd.DataFrame.from_dict(data=produceOD, orient="index")
df6 = pd.DataFrame.from_dict(data=nutOD, orient="index")
df7 = pd.DataFrame.from_dict(data=breadOD, orient="index")

writer = pd.ExcelWriter("shoppingList.xlsx", engine="xlsxwriter")

df5.to_excel(writer, sheet_name="Sheet1", header=False)

df1.to_excel(writer, sheet_name="Sheet1", header=False, startcol=3)
df6.to_excel(writer, sheet_name="Sheet1", header=False, startrow=(len(meatDairyEggsList) + 2), startcol=3)
df3.to_excel(writer, sheet_name="Sheet1", header=False, startrow=(len(meatDairyEggsList)+len(nutList)+4), startcol=3)

df4.to_excel(writer, sheet_name="Sheet1", header=False, startcol=6)
df7.to_excel(writer, sheet_name="Sheet1", header=False, startrow=(len(spiceList)+2), startcol=6)
df2.to_excel(writer, sheet_name="Sheet1", header=False, startrow=(len(spiceList) + len(breadList) + 4), startcol=6)

writer.save()

sys.stdout = open("recipesChosen.txt", "w")
pprint.pprint(shoppingList)
sys.stdout.close()