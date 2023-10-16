#Write a Python program to combine two dictionary by adding values for common keys.

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 208, 'd': 400}


result_dict = {}


for key, value in d1.items():
    result_dict[key] = result_dict.get(key, 0) + value


for key, value in d2.items():
    result_dict[key] = result_dict.get(key, 0) + value


print(result_dict)