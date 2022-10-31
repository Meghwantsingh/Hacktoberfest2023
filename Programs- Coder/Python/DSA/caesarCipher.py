#covert the given text to caesar cipher

def encrypt(string,increase):

    new_str=""

    for i in range(len(string)):

        if(ord(string[i])+increase)>90:

         new_str+=chr((((ord(string[i])+increase)-65)%26)+65)

        else:
            new_str+=chr(ord(string[i])+increase)

    return new_str

string=input()
increase=int(input())
print(encrypt(string,increase))