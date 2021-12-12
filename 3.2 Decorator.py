def flat_generator(a: list) -> list:
    return [x for sublist in a for x in sublist]

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	['g', 'h', 'h'],
]

print('Original list:', nested_list)
print('Transformed list:')
for item in  flat_generator(nested_list):
    print(item)