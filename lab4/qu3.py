def logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__}(){args}{kwargs} -> {result}")
        return result
    return wrapper
@logger
def reader(filename):
    file = open(filename, 'r')
    
    
    def next_line():
        return file.readline().strip() or None
    
    return next_line

get = reader('test.txt')
print(get())  
print(get())
print(get())