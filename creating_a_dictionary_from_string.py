#Write a Python program to create a dictionary from a string
string_ = input()
count_ = {}
for char in string_:
    if char.isalpha():
        char = char.lower()
        count_[char] = count_.get(char, 0) + 1
print(count_)