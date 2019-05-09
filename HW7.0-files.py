with open('cook-book.txt') as f:
    for line in f:
        cook_book = {}
        dish = line.strip()
        cook_book[dish] = []
        ingredient_num = f.readline().strip()
        ingredient_list = f.readline().split('|')
        next_line = f.readline()
        while next_line != '\n':
            ingredient_dict = {}
            ingredient_dict['ingredient_name'] = ingredient_list[0]
            ingredient_dict['quantity'] = ingredient_list[1]
            ingredient_dict['measure'] = ingredient_list[2]
            cook_book[dish].append(ingredient_dict)
            f.readline()

print(cook_book)
