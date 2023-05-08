import os
from datetime import datetime

def logger(old_function):
    def new_function(*args, **kwargs):
        time_ = datetime.now()
        value = old_function(*args, **kwargs)
        with open('main.log', 'a+', encoding='utf-8') as file:
            file.write(f'{time_} | {old_function.__name__} | {args=} | {kwargs=} | {value}\n')
        return value
    return new_function


def test_1():
    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return 'Error: division by zero'

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'
    result = div(6, 0)
    assert result == 'Error: division by zero', 'Деление на ноль должно вызвать ошибку'

    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(a=0, b=0)
    summator(4.3, b=2.2)

    with open(path, 'r') as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()