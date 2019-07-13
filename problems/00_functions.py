
# def fahrenheit_to_kelvin(x):
#     k = (5/9)*(x + 459.67)
#     return round(k, 2)
# exec(input())

# print(f"{fahrenheit_to_kelvin(23):.2f}")

# _________________________________________________________________Fahrenheit to Kelvin

# def centimeters_to_inches(x):
#     c = x / 2.54
#     return round(c, 3)
# exec(input())
# print(centimeters_to_inches(10))

# _________________________________________________________________Centimeters to inches

# def cal_centripetal_force(m, s, r):
#     ans = m*(s**2)/r
#     return round(ans,2)
# exec(input())

# _________________________________________________________________Centripetal force

# import math

# def cal_volume_cone(r,h):
#     v = (1/3)*(r**2)*h*math.pi
#     return round(v,2)
# exec(input())

# _________________________________________________________________Volume of Cone 

# def buddhist_era_to_rattanakosin_era(p):
#     c = p - 2324
#     return c
# exec(input())

# print(buddhist_era_to_rattanakosin_era(3600))

# _________________________________________________________________Convert Buddhist Era to Rattanakosin Era

# def average(listx):
    
#     for i in listx :
#         if type(i) != int :
#             return '\'This is not a list of integers.\''   
            
#     ave = sum(listx)/len(listx)
#     return round(ave,1)
# exec(input())

# print(average([1, 2, 3,'cat']))

# _________________________________________________________________Average

# dictx = {"a":1,"b":1}
# dictx["c"]=3
# print(dictx["d"])

# _________________________________________________________________Counting words

# import string

# def foo(text: str):
#         for i in text:
#                 if i in string.punctuation:
#                         text = text.replace(i,'')
#                 elif i in string.digits:
#                         text = text.replace(i,'')
#         text = text.split(" ")
#         Dick = {}
#         for i in text:
#                 if i not in Dick :
#                         Dick[i] = 1
#                 elif i in Dick:
#                         Dick[i] += 1
#         return Dick
        
# exec(input())
# x = foo("""Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.

# Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming. Python is often described as a "batteries included" language due to its comprehensive standard library.

# Python was conceived in the late 1980s as a successor to the ABC language. Python 2.0, released 2000, introduced features like list comprehensions and a garbage collection system capable of collecting reference cycles. Python 3.0, released 2008, was a major revision of the language that is not completely backward-compatible, and much Python 2 code does not run unmodified on Python 3. Due to concern about the amount of code written for Python 2, support for Python 2.7 (the last release in the 2.x series) was extended to 2020. Language developer Guido van Rossum shouldered sole responsibility for the project until July 2018 but now shares his leadership as a member of a five-person steering council.

# Python interpreters are available for many operating systems. A global community of programmers develops and maintains CPython, an open source reference implementation. A non-profit organization, the Python Software Foundation, manages and directs resources for Python and CPython development.""")

# print(x)