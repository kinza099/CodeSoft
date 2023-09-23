#  code by kinza

import random
character='abcdefghijklmopqrstuvwxyzABCDEFGHIJKLMOPQRSTUVWXYZ0123456789!@#$%^&*_'
length_of_password=int(input('Enter the length of password:'))
count_of_password=int(input('Enter the number of passwords'))

for i in range(0,count_of_password):
    password=""
    for j in range(0,length_of_password):
        pass_characters=random.choice(character)
        password+=pass_characters
    print(f"The random generated password is {password}")
