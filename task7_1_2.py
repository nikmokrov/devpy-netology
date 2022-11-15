def read_cookbook():
    with open('recipes.txt') as file:
        data = [line.strip() for line in file.readlines()]
    cook_book = {}
    new_recipe = True
    for i in range(len(data)):
        if data[i] == '':
            new_recipe = True
            continue
        if new_recipe:
            cook_book[data[i]] = [{'ingredient_name': data[i+2+s].split('|')[0].strip(),
                                   'quantity': int(data[i+2+s].split('|')[1].strip()),
                                   'measure': data[i+2+s].split('|')[2].strip()}
                                  for s in range(int(data[i+1]))]
            i += int(data[i+1])
            new_recipe = False
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read_cookbook()
    ingredients = {}
    for dish in dishes:
        # print(cook_book[dish])
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            ingredients.setdefault(ingredient_name, {})
            ingredients[ingredient_name] = {'measure': ingredient['measure'],
                                            'quantity': ingredients[ingredient_name].get('quantity', 0) +
                                                        ingredient['quantity'] * person_count}
    return ingredients


print('Cookbook:')
print(read_cookbook())
print('Ingredients:')
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
