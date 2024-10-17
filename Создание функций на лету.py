# 1 задание
first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second)))

# 2 задание

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a') as f:
            try:
                f.write(data_set)
            except TypeError as exc:
                f.write(str(data_set))
                print(f'Перевёл {data_set} в строку, ошибка: {exc}')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# 3 задание
from random import choice

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return(choice(self.words))

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())