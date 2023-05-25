# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов..


def double_list(array: list[int]) -> list[int]:
    res = set()
    for el in array:
        counter = array.count(el)
        if counter > 1:
            res.add(el)
    return list(res)


print(double_list([2, 2, 3, 3, 4]))


# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

import string

with open('example.txt', 'r', encoding='UTF-8') as file:
    data = file.read()

for char in string.punctuation:
    data = data.lower().replace(char, ' ')

counter_dict = {}

for word in data.split():
    counter_dict[word] = counter_dict.get(word, 0) + 1

counter_dict = tuple(sorted(counter_dict.items(), key=lambda item: item[1]))
for index, word in enumerate(counter_dict[-1:-10:-1], 1):
    print(f'{index}. {word[0]:>10} {word[1]} раз')
print(most_frequent(text))

# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

carrying_capacity = int(input('Введите грузоподъемность рюкзака: '))

list_of_equipment = {'Провиант': 3,
                     'Вода': 2,
                     'Палатка': 6,
                     'Мяч': 0.5,
                     'Шампура': 1,
                     'Одежда': 5,
                     'Снасти': 2.5,
                     'Алкоголь': 7,
                     'Топор': 3.5,
                     'Телевизор': 25}


def sort_list(some_set: set):
    global global_list
    if len(some_set) == 1:
        return some_set
    else:
        for item in some_set:
            new_set = some_set.copy()
            new_set.remove(item)
            global_list.add(tuple(sort_list(new_set)))
    return some_set


list_of_equipment = dict(sorted(list_of_equipment.items(), key=lambda x: x[1]))
global_list = {tuple(list_of_equipment)}
sort_list(set(list_of_equipment))

print(f'В рюкзак грузоподъемностью {carrying_capacity}кг может влезть:')

for stack in global_list:
    summ_stack = 0
    for item in stack:
        summ_stack += list_of_equipment.get(item)
        if summ_stack > carrying_capacity:
            break
    else:
        print(*stack, 'весом', summ_stack, 'кг')
