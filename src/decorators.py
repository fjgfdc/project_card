from functools import wraps


def log(filename=""):
    """
             Декоратор для логирования вызовов функции.

             Параметры:
             filename (str): Имя файла для логирования. Если не указано, логирование происходит в консоль.
             """
    def log_wrapper(func):
        @wraps(func)
        def log_inner(*args, **kwargs):
            try:
                massage = f"{func.__name__} ok"
                result = func(*args, **kwargs)
                if not filename:
                    print(f"{massage}")
                else:
                    with open(filename, "w") as file:
                        file.write(f"{massage}\n")
                return result
            except Exception as e:
                massage_error = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"
                if not filename:
                    print(f"{massage_error}")
                else:
                    with open(filename, "w") as file:
                        file.write(f"{massage_error}\n")
        return log_inner
    return log_wrapper


@log(filename="../mylog.txt")
def my_function(x, y):
    """Возвращает значение и записывает коректность работы функции в mylog.txt"""
    return x + y


my_function(1, 2)
