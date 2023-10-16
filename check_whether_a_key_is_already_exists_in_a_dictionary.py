#Write a Python script to check whether a given key already exists ina dictionary
main_dictionary ={8: 10, 1: 20, 2: 30}
checking_key = int(input("enter a key: "))
if checking_key in main_dictionary:
    print("The key is exists in the dictionary.")
else:
    print("The key is not exists in the dictionary.")