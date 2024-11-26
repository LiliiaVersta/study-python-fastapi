# Виведення значень за ключами
dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print(dict_test['car'])    # Toyota
print(dict_test['where'])  # EU

# Виведення ключів і значень
print(dict_test.keys())    # dict_keys(['car', 'price', 'where'])
print(dict_test.values())  # dict_values(['Toyota', 4900, 'EU'])

# Виведення пар ключ - значення
print(dict_test.items())   # dict_items([('car', 'Toyota'), ('price', 4900), ('where', 'EU')])