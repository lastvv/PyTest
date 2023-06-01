# ✔ Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.
abs_path = r'C:\Thecode\Media\статья.txt'


def split_path(abs_path: str) -> tuple():
    list_abs_path = abs_path.split('\\')
    list_last_elem = list_abs_path[-1].split('.')
    path = '\\'.join(list_abs_path[0:-1])
    name = list_last_elem[0]
    expansion = list_last_elem[1]
    return path, name, expansion


print(split_path(abs_path))

# ✔ Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии
name_employee = ('Кирилл Панфилов', 'Андрей Беляев', 'Виталий Кузьмин')
salary = (100000, 150000, 5000)
bonus = ('2.5%', '1.5%', '5%')

bonus = {name_employee[i]: salary[i] + salary[i] * (float(bonus[i][:-1]) / 100) for i in range(len(name_employee))}

print(bonus)

# ✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию)
def fib(n: int) -> list[int]:
    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b


print(*(fib(10)))





