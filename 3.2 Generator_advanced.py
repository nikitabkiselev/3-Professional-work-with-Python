def flat_generator(nested):
    try:
        it = iter(nested)
    except TypeError: # not an iterable
        yield nested
        return
    try:
        first = next(it)
    except StopIteration: # empty
        return
    yield from flat_generator(first)
    yield from flat_generator(it)

nested_list = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]

print('Original list:', nested_list)
print('Transformed list:')
for item in  flat_generator(nested_list):
    print(item)