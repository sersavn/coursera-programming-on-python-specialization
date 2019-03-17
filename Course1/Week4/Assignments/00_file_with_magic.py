'''
В этом задании вам нужно создать интерфейс для работы с файлами. Класс File должен поддерживать несколько необычных операций.

Класс инициализируется полным путем.
obj = File('/tmp/file.txt')

Класс должен поддерживать метод write.
obj.write('line\n')

Объекты типа File должны поддерживать сложение.
first = File('/tmp/first')
second = File('/tmp/second')
new_obj = first + second

В этом случае создается новый файл и файловый объект, в котором содержимое второго файла добавляется к содержимому первого файла. Новый файл должен создаваться в директории, полученной с помощью tempfile.gettempdir. Для получения нового пути можно использовать os.path.join.

Объекты типа File должны поддерживать протокол итерации, причем итерация проходит по строкам файла.
for line in File('/tmp/file.txt'):

И наконец, при выводе файла с помощью функции print должен печататься его полный путь, переданный при инициализации.
obj = File('/tmp/file.txt')
print(obj)
'/tmp/file.txt'

Опишите свой класс в скрипте и загрузите на платформу.
'''

import tempfile
import os

class File:

    def __init__(self, full_path):
        self.full_path = full_path
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            with open(str(self.full_path), 'r') as f:
                lines = f.readlines()[self.current]
                self.current += 1
                return lines
        except:
            raise StopIteration

    def __str__(self):
        return self.full_path

    def __add__(self, obj):
        temp_dir = tempfile.gettempdir()
        concated_file = "combined.txt"
        abs_path = os.path.join(temp_dir, concated_file)
        with open(abs_path, 'w') as main_f:
            with open(self.full_path, 'r') as f:
                main_f.write(f.read())
            with open(obj.full_path, 'r') as f:
                main_f.write(f.read())
        return File(abs_path)

    def write(self, data_to_write):
        with open(self.full_path, 'w') as f:
            f.write(data_to_write)

    def show(self):
        with open(self.full_path, 'r') as f:
            content = f.readlines()
            return content

'''
file_1 = File('test.txt')
file_2 = File('test_2.txt')

print(file_1)
print(type(file_1))
sum_file = file_1 + file_2
print(sum_file)
'''
