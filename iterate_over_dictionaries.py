#Write a Python program to iterate over dictionaries using for loops.
dictionary_ = {"name":"Rajesh", "age": 24, "gender": "male "}
for key in dictionary_:
    value = dictionary_[key]
    print(key,value)