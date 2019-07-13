# n = int(input('Put an integer here: '))
# x = 1

# while n >= x :
#     print('\nthe current number is',x)
#     y = x
#     x += 1
#     while n >= y :
#         print(y,end=',')
#         y += 1

# _________________________________________________________________Print number with loop

# n = int(input('Countdown from '))
# while n >= 0 :
#     print(n)
#     n -= 1

# _________________________________________________________________Countdown

# n = int(input('Number: '))
# x = 0
# while n >= x :
#     print(x,end=" ")
#     x += 2

# _________________________________________________________________Print even number

# n = int(input('Number: '))
# x = 1
# while n >= x :
#     print(x,end=" ")
#     x += 2

# _________________________________________________________________Print odd number

# n = int(input('How many times?: '))
# x = 1
# if n > 0 :
#     while n >= x :
#         print('Hello!')
#         x += 1
# else :
#     print('Input number must be a positive integer.')

# _________________________________________________________________Say hello n times

# x = input('Enter text: ')
# listx = list(x)
# print('A length of this text is',len(listx))

# _________________________________________________________________Find a length of input string

# x = 0
# while x < 18:
#     x = int(input('How old are you? '))
# print('Congratulation! You can vote in the election.')

# _________________________________________________________________Election

# x = 0
# y = 0
# while y < 100:
#     x = float(input('Enter a number: '))
#     y = x + y
# print(f'Summation = {y:.2f}')

# _________________________________________________________________Sum of an input number

# import string
# x = (list(input('Enter text: ')))
# y = 0

# for i in x :
#         c = i in string.punctuation
#         if i.isupper() == True or i.isnumeric() == True or c == True :
#                 y +=1

# print(f'There is(are) {y} uppercase(s).')
# _________________________________________________________________
# a=input("Enter text: ")
# i=0

# for s in a:
#     if s==" ":
#         i=i
#     elif s==s.upper():
#         i+=1

# print(f"There is(are) {i} uppercase(s).")

# _________________________________________________________________Count uppercase

# import string

# x = list(input('Enter text: '))
# y = 0
# for i in x :
#         c = i in string.punctuation
#         if i.islower() or i.isnumeric() or c :
#                 y +=1

# print(f'There is(are) {y} lowercase(s).')
# _________________________________________________________________
# a=input("Enter text: ")
# i=0

# for s in a:
#     if s==" ":
#         i=i
#     elif s==s.lower():
#         i+=1

# print(f"There is(are) {i} lowercase(s).")

# _________________________________________________________________Count lowercase

# import string
# x = list(input('Enter your text: ').lower())
# x = set(x)
# y = 0

# for i in x :
#     if i in string.ascii_lowercase :
#         print(i)
#         y +=1
#     else : y = y
        
# print(f'This text has {y} consonant(s).')

# _________________________________________________________________

# import string
# x = set(input('Enter your text: ').lower())
# y = 0
# for i in x :
#     if i in (string.ascii_lowercase) :
#         y +=1
#     else : y = y
        
# print(f'This text has {y} consonant(s).')

# _________________________________________________________________Count consonants

# x = int(input('Enter a size of square: '))

# for i in range(x):
#         print('+ '*x)
# _________________________________________________________________Make Square

# n = int(input("Specify n: "))
# x = 0
# num1 = 1
# num2 = 0

# if n == 0 :
#         print("Fn = 0")
# else :
#         while x < n:
#                 num3 = num1+num2
#                 num1 = num2
#                 num2 = num3
#                 x = x+1
#         print("Fn =",num3)

# _________________________________________________________________Find the nth Fibonacci

# n = int(input("Specify the length of sequence: "))
# x = 0
# num1 = 1
# num2 = 0

# while x <= n:
#         num3 = num1+num2
#         num1 = num2
#         num2 = num3
#         x = x+1
#         print(num3,end=" ")
# print(f"\nfinal ratio = {num3} / {num1} = {num3/num1:.4f}")

# _________________________________________________________________Find the golden ratio from the Fibonacci sequence________________________________________________

# import string
# x = list(input("Plaintext: "))
# letters = "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz"
# rot13 = "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm"
# text = ''
# for i in x:
#     try:
#         z = letters.index(i)
#         text += rot13[z]
#     except:
#         text += i

# print(f'Ciphertext: {text}')

# _________________________________________________________________ROT13

# text = list(input('Input text: '))
# dd = ''
# for i in text :
#     dd += i*2
# print(dd)

# _________________________________________________________________Double character

# l = int(input('How many layers?  '))
# t = int(input('How many trees? '))
# x = l
# n = 0
# p = 1
# k = "+"

# while t > n :
#     n +=1
#     x = l
#     p = 1
#     while x > 0 :
#         # x = int(2*x)
#         # y = k*p
#         # print(f'{y:^x}')
#         print((" "*(x+1)+("+"*p)+(" "*(x+1))))
#         x -= 1
#         p += 2

# _________________________________________________________________Christmas Tree

# A1 = False
# A2 = False

# while A1 == False:
#     Q1 = input('Quit the game without saving? (Y/n): ')
#     if Q1 == 'n' :
#         A1 = True
#         print('Thought so!')
#     elif Q1 == 'Y' :
#         A1 = True
#         while A2 == False :
#             Q2 = input('Are you sure? (Y/n): ')
#             if Q2 == 'n' :
#                 A2 = True
#                 print('Thought so!')
#             elif Q2 == 'Y' :
#                 A2 = True
#                 print('Thanks for playing!')
#             else :
#                 print('Invalid. The choice is case sensitive.')
#     else :
#         print('Invalid. The choice is case sensitive.')

# _________________________________________________________________Yes or No

# import string

# pwd = input('Enter your password: ')
# n = len(list(pwd))
# x = y = z = 0

# if n >= 8 and n < 20:
#     for i in pwd:
#         num = i in string.digits
#         eng = i in string.ascii_letters
#         spe = i in string.punctuation
#         if spe == True:
#             x += 1
#         elif eng == True:
#             y += 1
#         elif num == True:
#             z += 1
#     if x != 0 and y != 0 and z != 0:
#         print('Your password is very strong')
#     elif x == y == 0 or x == z == 0 or y == z == 0:
#         print('Your password is normal')
#     else:
#         print('Your password is strong')

# else:
#     print('Your password must be contained at least 8 alphabets and less than 20 alphabets')

# _________________________________________________________________Password Set

# num = int(input('Number: '))

# if num > 1:
#    for i in range(2, num//2):
#        if (num % i) == 0:
#            print(num, "is not a prime number.")
#            break
#    else:
#        print(num, "is a prime number.")
# elif num == 1:
#     print(num, "is not a prime number.")
# elif num == 0:
#     print(num, "is not a prime number.")
# else:
#     print("Input number must be a non-negative integer.")

# _________________________________________________________________Is a prime number?

# x = (list(input('Enter your text: ')))
# y = 0
# z = 0

# for i in x :
#     if i in "aeiouAEIOU" :
#         z += 1
#     elif i in "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz" :
#         y += 1

# print(f'This text has {y} consonant(s) and {z} vowel(s).')

# _________________________________________________________________Count consonants and vowels

# num = int(input('Input number: '))
# sum = 0

# print("Factors of",num,"are",end=" ")
# if num <= 0 :
#     print('None',end=" ")
#     print('\nSummation of factors is',sum)
# else:
#     for i in range(1, num + 1):
#         if num % i == 0:
#             print(i,end=" ")
#             sum = sum + i
#     print('\nSummation of factors is',sum)

# _________________________________________________________________Find factors

# x = 0
# num1 = int(input("Specify the first number: "))
# num2 = int(input("Specify the second number: "))
# n = int(input("Specify the length of sequence: "))

# print(num1,end=" ")
# for i in range(n-1):
#         num3 = num1+num2
#         num4 = num1
#         num1 = num2
#         num2 = num3
#         x = x+1
#         print(num1,end=" ")
# print(f"\nfinal ratio = {num1} / {num4} = {num1/num4:.4f}")

# _________________________________________________________________

import string

su = list(string.ascii_uppercase)
sl = list(string.ascii_lowercase)
dictL = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11,
 'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 
't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}
dictU = {'A': 1, 'C': 3, 'B': 2, 'E': 5, 'D': 4, 'G': 7, 'F': 6, 'I': 9, 'H': 8, 'K': 11,
 'J': 10, 'M': 13, 'L': 12, 'O': 15, 'N': 14, 'Q': 17, 'P': 16, 'S': 19, 'R': 18, 'U': 21, 
'T': 20, 'W': 23, 'V': 22, 'Y': 25, 'X': 24, 'Z': 26}
n = (int(input('Shift: ')))
x = (input("Plaintext: "))
text = ''

for i in x:
        if i in su:
            z = su.index(i)

            b = dictU[i] == ((z+n)%26)
            while b == True:
                text += dictU[i]
        elif i in sl:
            z = sl.index(i)
            b = dictL[i] == ((z+n)%26)
            while b == True:
                text += dictL[i]
        else:
            text += i
print(f'Ciphertext: {str(text)}')

# # for i in x:
# #     if i in su :
# #         try:
# #             z = text.index(i)
# #             text += su[z+n]
# #             print(i)
# #         except:
# #             text += i
# #     elif i in sl :
# #         try:
# #             z = text.index(i)
# #             text += sl[z+n]
# #             print(i)
# #         except:
# #             text += i
# #     elif i in sw or sp or sd :
# #         print(i)
# #         text += i
    
# print(f'Ciphertext: {text}')

# for i in x:
#     if i in su :
#         z = text.index(i)
#         text += su[z+n]
#         print(i)
#     elif i in sl :
#         z = text.index(i)
#         text += sl[z+n]
#     else :
#         text += i
    
# print(f'Ciphertext: {text}')

# _________________________________________________________________

