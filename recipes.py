from pprint import pprint

with open('recipes.txt') as f:
    cook_book = {}
    for line in f:
        line_1 = f.readline().strip('\n')
        line_2 = int(f.readline())
        counter = 0
        list_book = []
        while counter < line_2:
            line_3 = f.readline().split(' | ')
            counter += 1
            list_book.append({'ingredient_name' : line_3[0], 'quantity' : int(line_3[1]), 'measure' : line_3[2].strip('\n')})
        cook_book[line_1] = list_book

def get_shop_list_by_dishes(dishes, person_count):
    list_products = {}   
    for key, value in cook_book.items():
        if key in dishes:
            for product in value:
                list_products[product['ingredient_name']] = [f"{product['quantity'] * (person_count * dishes.count(key))}, {product['measure']}"]
    return list_products


def merge_files(files):
    result_1 = {}
    all_text = {}
    for my_file in files:
        with open(my_file) as text:
            counter = 0
            all_list = []
            for string in text:
                all_list.append(string)
                counter += 1
            result_1[counter] = my_file
            all_text[my_file] = all_list
    result_2 = sorted(result_1.items())
    with open('result.txt', 'w') as new_text:
        for element in result_2:
            new_text.write(f'{element[1]}\n')
            new_text.write(f'{str(element[0])}\n')
            new_text.write(f'{"".join(all_text.get(element[1]))}\n')
    return 'Запись завершена'
 

pprint(get_shop_list_by_dishes(['Омлет', 'Омлет', 'Запеченный картофель'], 2), sort_dicts=False)

print(merge_files(['1.txt', '2.txt', '3.txt']))