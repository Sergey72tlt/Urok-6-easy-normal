#Митягин Сергей уровень easy

# Задача-1:
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

# Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
path = os.getcwd()
os.chdir(path)
for i in range(1, 10):
    newfolder = 'Новая папка ' + str(i)
    os.makedirs(newfolder)

print('Папки созданы')


path = os.getcwd()
os.chdir(path)
for i in range(1, 10):
    newfolder = 'Новая папка ' + str(i)
    os.removedirs(newfolder)

print('Папки удалены')


# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.


os.listdir()
print(os.listdir())

# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil


def current_file_copy ():
    name_file = os.path.realpath(__file__)
    new_file = name_file +'.copy'
    if os.path.isfile(new_file) != True:
        shutil.copy(name_file, new_file)
        return new_file + ' - создан'
    else:
        return 'Файл уже скопирован'

if __name__ == '__main__':
    print(current_file_copy())
