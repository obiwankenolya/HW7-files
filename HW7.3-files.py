with open('cook-book.txt') as f:

    def get_shop_list_by_dishes(dishes, person_count):
        def get_cook_book():
            cook_book = {}
            for line in f:
                ingredient_lines = 0
                dish = line.strip()
                ingredients_num = f.readline().strip()
                ingredient_list = f.readline().split('|')
                while ingredient_lines <= int(ingredients_num):
                    f.readline()
                    ingredient_dict = {}
                    ingredient_dict['ingredient_name'] = ingredient_list[0]
                    ingredient_dict['quantity'] = ingredient_list[1]
                    ingredient_dict['measure'] = ingredient_list[2]
                    cook_book[dish] = ingredient_dict
                    ingredient_lines += 1
                f.readline()
            return cook_book
        get_cook_book()

        ing_dict = {}
        for dish in dishes:
            if dish in cook_book.keys():
                for ingredient in cook_book[dish]:
                    if ingredient['ingredient_name'] in ing_dict.keys():
                        ing_dict[ingredient]['ingredient_name']['quantity'] += ingredient['quantity'] * person_count
                    else:
                        ing_dict[ingredient]['ingredient_name'] = {
                            'measure': ingredient['measure'],
                            'quantity': ingredient['quantity'] * person_count
                        }
        print(ing_dict)


    get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
