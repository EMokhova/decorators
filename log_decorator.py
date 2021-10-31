import datetime


def log_decorator_fabric(file_path):
    def log_decorator(old_function):
        def new_function(*arg, **kwargs):
            date_time = datetime.datetime.now()
            func_name = old_function.__name__
            result = old_function(*arg, **kwargs)
            log_line = f' {date_time}, Функция {func_name} c аргументами {arg}, {kwargs}. Результат: {result} \n'
            with open(file_path, 'a', encoding='utf-8') as f:
                f.write(log_line)
            return result
        return new_function
    return log_decorator
