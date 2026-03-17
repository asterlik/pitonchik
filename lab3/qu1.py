def unpack_recursive(data):
    if not data:
        return []
    if not isinstance(data, (list, tuple, set)):
        data = [data]
    
    first = data[0]
    rest = data[1:]
    
    if isinstance(first, (list, tuple, set)):
        return unpack_recursive(list(first)) + unpack_recursive(rest)
    elif isinstance(first, dict):
        return unpack_recursive(list(first.keys())) + unpack_recursive(list(first.values())) + unpack_recursive(rest)
    elif first is not None:
        return [first] + unpack_recursive(rest)
    else:
        return unpack_recursive(rest)


test_data = [None, [1, ({2, 3}, {'foo': 'bar'})]]
print("распаковка:")
print("рекурсия:", unpack_recursive(test_data))