# def asking():
#     x = input('Input an integer: ')
#     runtest(x)

# def runtest(x):
#     try:
#         val = int(x)
#     except ValueError:
#         print('Invalid input.')
#         asking()

# print(asking())

# _________________________________________________________________

# def ask():
#     lx = (input('Input an integer: '))
#     return check(lx)

# def check(x):
#     for i in x :
#         print(x)
#         if type(i) != int :
#             return type(i) #ask()

# listx = list(input('Input an integer: '))
# print(check(listx))

# _________________________________________________________________

# x = int(input('Specify row(s): '))
# y = int(input('Specify column(s): '))

# while x >= 0:
#     print("+---"*y,end='+\n')
#     if x > 0:
#         print("|   "*(y+1))
#     x -=1

# _________________________________________________________________Draw Table

# def fibonacci(n) :
#     num1 = 1
#     num2 = 0
#     x = 0
#     if n == 0 :
#         return 0
#     else :
#             while x < n:
#                 num3 = num1+num2
#                 num1 = num2
#                 num2 = num3
#                 x = x+1
#             return num3

# exec(input())
# print(fibonacci(16))

# _________________________________________________________________Find the nth Fibonacci (recursion)

# import string
# x = input('Input a number: ')
# c = [x for x in string.ascii_letters]
# for i in c:
#     while i == x:
#         x = input('Input a number: ')
#         c = x in string.ascii_letters

# try:
#     print(a)
# except NameError:
#         print(5)

# a = input("ENter some number : ")

# try:
#         print(float(a))
# except ValueError:
#         print("Invalid")

# # print(int(a))

# Input a number: three
# Incorrect input.

# _________________________________________________________________note

# c = False
# while c == False:
#         try:
#                 x = (input("Input an integer: "))
#                 if "," in x :
#                         x = x.replace(",","")
#                 else :
#                         x = x.replace(" ","")
#                 x = int(x)
#                 c = True
#         except:
#                 print('Invalid input.')

# _________________________________________________________________Get a numeric input (machine readable)

# c = False
# while c == False:
#         try:
#                 x = (input('Input a number: '))

#                 if "," in x and " " in x:
#                         x = x.replace(",",".")
#                         x = x.replace(" ","")
#                         x = float(x)
#                         print(x)
#                         c = True
#                 elif "," in x and "." in x :
#                         x = x.replace(",","")
#                         x = float(x)
#                         print(x)
#                         c = True
#                 elif "," in x :
#                         x = x.replace(",","")
#                         if float(x) >= 1000:
#                                 x = float(x)
#                                 print(x)
#                                 c = True
#                         else :
#                                 print('Invalid input.')
#                 elif " " in x :
#                         x = x.replace(" ","")
#                         x = float(x)
#                         print(x)
#                         c = True
#                 else :
#                         x = float(x)
#                         print(x)
#                         c = True
#         except:
#                 print('Invalid input.')

# _________________________________________________________________Get an integer input (human and machine readable)

# print_directory({'Foo': [
#                 {'Bar': [
#                 {'Fizz': []},
#                 {'Buzz': []}]},
#                 {'Bazz': []}
# ]})

# Foo
# ├── Bar
# │   ├── Fizz
# │   └── Buzz
# └── Bazz

# def print_directory(MainHeading : [subHeading]) :
#         print(MainHeading)
#         print('├──',end=" ")
#         return (print_directory(subHeading : []))


# def print_directory(dictx):
#         print(type(dictx)
#         # print('├──',end=" ")
#         # if dictx.values == 0:
#         #         return
#         return # 5(print_directory(dictx.values))

# x = print_directory({'Foo': [{'Bar': [{'Fizz': []},{'Buzz': []}]},{'Bazz': []}]})
# print(x)

# _________________________________________________________________

# def tetrate(a:int,n:int):
#         if n == 1 :
#                 return a
#         return a ** tetrate(a, n-1)
# # exec(input())


# print(tetrate(2,-1))


# def tetrate(a,n):
#     if n == 0 :
#         return 1
#     if n > 0 :
#         return a ** tetrate(a, n-1)
#     raise ValueError('math domain error')
# exec(input())

# print(tetrate(2,2))

# _________________________________________________________________

# print_pascal(5)
#            1 
#          1   1 
#        1   2   1 
#      1   3   3   1 
#    1   4   6   4   1 
#  1   5  10  10   5   1 



def print_pascal(n):
    listx = [0]
    for i in range(1,n+1) :
        listx.append(1)
        print(i)
        a = 0
        listy=[]         
        while len(listy) < i :
            x = listx[a]+listx[a+1]
            a += 1
            listy.append(x)                
            print(listy)
        for i in listy:
            listx.append(i)
        listx.append(1)


    return listx



print(print_pascal(4))

# def print_pascal(n):
#         x = 0
#         p = 1
#         txt = '1'
#         while n >= 0 :
#                 n -= 1
#                 print(((n+1)*"   ")+txt)
#                 txt = ("1   "+txt+"   1")


















