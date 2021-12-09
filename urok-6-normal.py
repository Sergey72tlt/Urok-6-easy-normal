#Митягин Сергей уровень normal

# Задача-1:
# Примечание: Если уже делали easy задание, то просто перенесите решение сюда.
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:
def avg(a, b):
    """Вернуть среднее геометрическое чисел 'a' и 'b'.

    Параметры:
        - a, b (int или float).

    Результат:
        - float.
    """
    return (a * b) ** 0.5

try:
    a = float(input("a = "))
    b = float(input("b = "))
    c = avg(a, b)
    print("Среднее геометрическое = {:.2f}".format(c))
except Exception:
    print('неверно введено число')


# ПРИМЕЧАНИЕ: Для решения задачи 2-3 необходимо познакомиться с модулями os, sys!
# СМ.: https://pythonworld.ru/moduli/modul-os.html, https://pythonworld.ru/moduli/modul-sys.html

# Задача-2:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь "меню" выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import os

def print_help():
    print('1. перейти в папку')
    print('2. посмотреть содержимое текущей папки')
    print("3. удалить папку" )
    print("4. создать папку")
    print("Чтобы выйти нажмите Enter")

def make_dir():
    directory = input('Enter directory name: ')
    if not directory:
        print("Укажите диреторию")
        return
    dir_path = os.path.join(os.getcwd(), directory)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(directory))
    except FileExistsError:
        print('директория {} уже существует'.format(directory))

def make_del_dir():
    directory = input('Enter directory name: ')
    if not directory:
        print("Укажите диреторию")
        return
    dir_path = os.path.join(os.getcwd(), directory)
    try:
        os.rmdir(dir_path)
        print('директория {} удалена'.format(directory))
    except FileExistsError:
        print('директория {} не существует'.format(directory))

def look_dir():
    print(os.listdir())

def change_dir():
    directory = input('Enter directory name: ')
    if not directory:
        print('Необходимо указать имя директории')
        return
    try:
        os.chdir(directory)
        print('Успешно перешли в папку: {}'.format(directory))
        print('Текущий каталог: ', os.getcwd())
    except FileNotFoundError:
        print('{} - папки не существует'.format(directory))




do = {
    '1': change_dir,
    '2': look_dir,
    '3': make_del_dir,
    '4': make_dir,
    }


print_help()
key = input('Choose: ')

if key:
    if do.get(key):
        do[key]()
    else:
        print('wrong key')
        print('write help to get help')