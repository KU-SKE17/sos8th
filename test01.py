# รับค่า input_01
# x = input("Enter your name? ")
# y = input("Enter your school? ")
# z = input("Enter your age? ")
# v = input("Enter your BD? ")

# nomal_print
# print('\nMy name is %s.\nMy last school is %s.\nI\'m%s year old.\nMy briday is %s.\n' %(x,y,z,v))

# f_func
# print(f'\n{x}\n{y}\n{z}\n{v}\n')

# float .2f
# x = float(input("Celsius: "))
# print(f"{x:.2f} Celsius is {x+273.15:.2f} Kelvin.")

# _________________________________________________________________

# import math

# print()
# print(4.2)
# print()
# print(math.ceil(4.2))
# print()
# print(math.floor(4.2))

# print()
# print(math.factorial(10))

# print()
# # เปลี่ยน rad เป็น degree
# print(math.sin(30*math.pi/180))

# _________________________________________________________________

# people = int(input('How many people?: ') )
# price = int(input('What is the ticket price? (4500/2500/1500): ') )
# print('Total price is', people*price )
# _________________________________________________________________

# import math

# x = float(input("Enter an angle(degrees): "))
# print(f'From an angle {x:.2f} degrees')
# print(f'sin({x:.2f}) = {math.sin(x*math.pi/180):.2f}')
# print(f'cos({x:.2f}) = {math.cos(x*math.pi/180):.2f}')
# print(f'tan({x:.2f}) = {math.tan(x*math.pi/180):.2f}')

# _________________________________________________________________

# a = float(input('The length of side a: '))
# b = float(input('The length of side b: '))
# if a <= 0 or b <= 0 :
#      print('Side a and side b must be greater than 0')
# elif a == b == 0 :
#      print('Side a and side b must be greater than 0')
# else:
#      print(f'The longest side is {(((a**2)+(b**2))**(1/2)):.3f}')

# _________________________________________________________________

# import math

# x = int(input("Number of factorial: "))
# xF = math.factorial(x)
# print(f'{x}! = {xF}')

# _________________________________________________________________

# i = float(input('Vector i: '))
# j = float(input('Vector j: '))
# k = float(input('Vector k: '))

# print(f'From vector <{i},{j},{k}>')

# print(f'The magnitude of this vector is {(((i**2)+(j**2)+(k**2))**(1/2)):.2f}')
# _________________________________________________________________

# x = int(input('Enter first integer: '))
# y = int(input('Enter second integer: '))

# print(x+y)
# print(x-y)

# _________________________________________________________________

# import math
# num = float(input('Enter number : '))

# print(math.ceil(num))
# print(math.floor(num))
# print(round(num))

# _________________________________________________________________

# x = float(input('Degrees: '))
# ans = (x*0.01745)
# print(f'{x:.2f} degrees is {ans:.2f} radians.')
# _________________________________________________________________

# x = float(input('Thai Baht: '))
# ans1 = x * 0.029
# ans3 = x * 37.64
# ans2 = x * 3.47

# print(f'{x:.2f} Baht is {ans1:.2f} Euro, {ans2:.2f} Yen and {ans3:.2f} Won.')
# _________________________________________________________________

# x = float(input('Enter mass(kg) = '))
# y = float(input('Enter acceleration(m/s^2) = '))

# print(f'From mass = {x:.2f} kg and acceleration = {y:.2f} m/s^2')
# print(f'Total force = {x*y:.2f} N')

# _________________________________________________________________

# x = int(input('Specify row(s): '))
# y = int(input('Specify column(s): '))

# while x >= 0:
#     print("+---"*y,end='+\n')
#     if x > 0:
#         print("|   "*(y+1))
#     x -=1

# _________________________________________________________________

# x = 12

# if 1 < x < 15 :
#     print('1 < x < 15')
# elif  x > 0 :
#     print('x > 0')

# _________________________________________________________________

# import string

# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)

# import string

# sl = list(string.ascii_lowercase)
# dictL = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11,
#  'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21,
# 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}
# for i in sl:
#     print(dictL[i])

# _________________________________________________________________

# gg=[1,2,3,4,5]
# ll=[99,88,77]
# for i in gg:
#     ll.append(i)
# print(ll)
# ff =[]
# print(type(gg))
# print(gg[1]+gg[0])
# z = gg[1]+gg[0]
# ff.append(z)
# print(ff)

# print(gg.index(2))
# print(str(gg))

# for i in gg:
#     print(i)
#     gg = gg.append(gg[i]+gg[i+1])

# _________________________________________________________________

listx=[1,2,3,4,5]
a = 0
listy = []
while len(listy) < 4:
    x = listx[a]+listx[a+1]
    a += 1
    listy.append(x)
print(listy)

# _________________________________________________________________