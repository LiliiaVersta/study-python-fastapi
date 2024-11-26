# Перетворення числа в рядок
num_str = 125
num_str = str(num_str)

# Заміна символів у рядку
message = 'Hi, my name is Python!'
message = message.replace('y', '0').replace('i', '1')
print(message)  # H1, m0 name 1s P0thon!

# Розділення рядка та обʼєднання
split_test = 'This is a split test'
split_list = split_test.split()  # ['This', 'is', 'a', 'split', 'test']
string_join = " ".join(split_list)
print(string_join)  # This is a split test

# Визначення довжини рядка
print(len(string_join))  # 20