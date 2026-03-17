def unpack_iterative(data):
    result = []
    stack = list(data)
    while stack:
        item = stack.pop()
        if isinstance(item, (list, tuple, set)):
            stack.extend(item)
        elif isinstance(item, dict):
            stack.extend(item.keys())
            stack.extend(item.values())
        elif item is not None:
            result.append(item)
    return result[::-1]

test_data = [None, [1, ({2, 3}, {'foo': 'bar'})]]
print("распаковка:")
print("итеративно:", unpack_iterative(test_data))