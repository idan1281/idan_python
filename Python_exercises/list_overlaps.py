import random
list_a = [random.randint(0, 20) for r in range(10)]
list_b = [random.randint(0, 30) for r in range(8)]
common_list = []
for i in list_a:
    if i in list_b and i not in common_list:
        common_list.append(i)
for i in list_b:
    if i in list_a and i not in common_list:
        common_list.append(i)

print(common_list)

print(list_a)
print(list_b)