# Додавання елементів у список
list_append = [1, 2, 3]
list_append.append(4)
list_append.append(5)
print(list_append)  # [1, 2, 3, 4, 5]

# Розширення списку
list_extend = [4, 5, 6]
list_extend.extend([7, 8, 9])
print(list_extend)  # [4, 5, 6, 7, 8, 9]

# Індекс елемента
index_of_6 = list_extend.index(6)
print(index_of_6)  # 2

# Довжина списку
print(len(list_append))  # 5