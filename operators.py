# Порівняння чисел
print(integer_var > float_var)       # False
print(integer_var == 42)             # True

# Порівняння рядків
print("abc" < "bcd")                 # True
print("Python" == "Python")          # True

# Порівняння булевих значень
print(bool_var == False)             # False
print(True != False)                 # True

# Порівняння списків
print(list_var == [1, 2, 3, 4])      # True
print(list_var != [4, 3, 2, 1])      # True

# Порівняння словників
print(dict_var == {"key": "value"})  # True
print(dict_var != {"key": "other"})  # True

# Порівняння кортежів
print(tuple_var == (1, 2, 3))        # True
print(tuple_var < (1, 2, 4))         # True