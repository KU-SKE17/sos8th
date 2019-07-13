# person = {
#     "name": "dd",
#     "age": 18,
#     "gender": "female"
# }
# print(person)
# print(len(person))
# result = person.pop("age")
# print(result)
# print(person)
# dict_key1 = person.keys()
# dict_value1 = person.values()
# print(list(dict_key1))
# print(type(list(dict_key1)))
# print(dict_value1)
# print(type(dict_value1))

# _________________________________________________________________


# _________________________________________________________________
# _________________________________________________________________
# _________________________________________________________________
# _________________________________________________________________

# แสดงผลตัวท้ายสุดของ dict
# dict123 ={
#     "dd" : "tall",
#     "yeg" : "cute",
#     "sese" : "somewhat"
# }
# # dict ไม่ใช้ list ดึงค่า index ไม่ได้
# print(list(dict123.values())[-1])

# _________________________________________________________________

# num = input('give me your note: ')
# num2 = num.split(",")
# num3 = set(num2)
# num4 = list(num3)
# num4 = sorted(num4)
# print(num4)

# _________________________________________________________________

def factorial(num):

    if num == 1 :
        return 1
    return num * factorial(num - 1)


print(factorial(10))