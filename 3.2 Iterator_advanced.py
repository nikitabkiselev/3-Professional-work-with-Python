nested_list = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
# список вывода
output = []
# функция, используемая для удаления вложенных
# списки в питоне.
def FlatIterator(nested_list):
    for i in nested_list:
        if type(i) == list:
            FlatIterator(i)
        else:
            output.append(i)
# Код драйвера
print('The original list: ', nested_list)
FlatIterator(nested_list)
print('The list after removing nesting: ', output)