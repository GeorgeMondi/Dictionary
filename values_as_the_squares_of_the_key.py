#write a Python script to print a dictionary where the keys are numbers between 1 and 15 (included)and the values are the square of the keys.
dictionary_={}
for num in range(1,16):
    dictionary_[num] = num ** 2
print(dictionary_)
