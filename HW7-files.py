with open('cook_book.txt') as f:
    cook_book = {}
    for line in f:
        ingredient_lines = 0
        meal = line.strip()
        num_of_ingredients = f.readline().strip()
        while ingredient_lines <= ingredient_lines:
            ingredient_dict = {}
            ingredient_list = line.split()
            starting_ingredient_list = line.split()
            del (ingredient_list[-1])
            if len(ingredient_list) == 2:
                ingredient = ingredient_list[0] + ' ' + ingredient_list[1]
            else:
                ingredient = ingredient_list[0]
            ingredient_dict['ingredient_name'] = ingredient
            ingredient_dict['quantity'] = starting_ingredient_list[-3]
            ingredient_dict['measure'] = starting_ingredient_list[-1]
            ingredient_lines += 1



print(cook_book)

