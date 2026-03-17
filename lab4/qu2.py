def logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__}{args}{kwargs} -> {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

add(a=2, b=3)