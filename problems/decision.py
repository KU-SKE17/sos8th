# r = int(input('How many Red Velvet Cakes?: '))
# p = int(input('How many Pana Cottas?: '))
# c = int(input('How many Cheese Pies?: '))
 
# if r>=0 and p>=0 and c>=0 :
#     Tp = r*130 + p*90 + c*145
#     Ts = Tp//100
#     print('Total price =',Tp)
#     print('Total stamps =',Ts)
# else :
#     print('Input number must be a positive integer.')

# _________________________________________________________________What is your payment and stamp? 

# x = int(input('Please enter integer: '))

# if x%2 == 0 :
#     print(x,'is even.')
# else :
#     print(x,'is odd.')

# _________________________________________________________________Is odd or even?

# x = float(input('Please enter angle(in degree unit): '))

# if x > 0 and x <= 360 :
#     if x < 90  :
#         print('Acute angle')
#     elif x == 90  :
#         print('Right angle')
#     elif x > 90 and x < 180  :
#         print('Obtuse angle')
#     elif x == 180  :
#         print('Straight angle')
#     elif x > 180 and x < 360  :
#         print('Reflex angle')
#     elif x == 360  :
#         print('Full rotation')
# else :
#     print('The angle must be larger than 0')

# _________________________________________________________________What kind of this angle?

# _________________________________________________________________Find n from Fn(เราไม่ได้ทำ)

# x = float(input('Enter base: '))
# y = float(input('Enter height: '))

# if x >= 0 and y >= 0 :
#     print(f'Area of triangle is {((1/2)*x*y):.2f}')
# else :
#     print('Base and height must be positive.')

# _________________________________________________________________Area of triangle

# x = input('What is your gender? (male/female): ')

# if x.lower() == 'male' :
#     print('Hello mister!')
# elif x.lower() == 'female' :
#     print('Hello miss!')
# else :
#     print('Input must be male or female.')

# _________________________________________________________________Say hello depending on the gender 

# a=int(input("Enter your birthday: "))
# b=input("Enter your birth month(Jan/Feb/Mar/Apr/May/Jun/Jul/Aug/Sep/Oct/Nov/Dec): ")

# if b=="Jan" or b=="Mar" or b=="May" or b=="Jul" or b=="Aug" or b=="Oct" or b=="Dec":
#     if a>31 or a<1:
#         print("There is no this day in this month.")
#     elif b=="Mar":
#         if a>20:
#             print("Your zodiac sign is Aries.")
#         else:
#             print("Your zodiac sign is Pisces.")
#     elif b=="May":
#         if a > 20:
#             print("Your zodiac sign is Gemini.")
#         else:
#             print("Your zodiac sign is Taurus.")
#     elif b == "Jul":
#         if a > 22:
#             print("Your zodiac sign is Leo.")
#         else:
#             print("Your zodiac sign is Cancer.")
#     elif b == "Aug":
#         if a > 22:
#             print("Your zodiac sign is Virgo.")
#         else:
#             print("Your zodiac sign is Leo.")
#     elif b == "Oct":
#         if a > 22:
#             print("Your zodiac sign is Scorpio.")

#         else:
#             print("Your zodiac sign is Libra.")
#     elif b == "Dec":
#         if a > 21:
#             print("Your zodiac sign is Capricorn.")

#         else:
#             print("Your zodiac sign is Sagittarius.")
#     elif b == "Jan":
#         if a > 19:
#             print("Your zodiac sign is Aquarius.")

#         else:
#             print("Your zodiac sign is Capricorn.")

# elif b=="Feb":
#     if a>28 or a<1:
#         print("There is no this day in this month.")
#     elif b == "Feb":
#         if a > 18:
#             print("Your zodiac sign is Pisces.")

#         else:
#             print("Your zodiac sign is Aquarius.")

# elif b=="Apr" or b=="Jun" or b=="Sep" or b=="Nov":
#     if a>30 or a<1:
#         print("There is no this day in this month.")
#     elif b == "Apr":
#         if a > 19:
#             print("Your zodiac sign is Taurus.")
#         else:
#             print("Your zodiac sign is Aries.")
#     elif b == "Jun":
#         if a > 20:
#             print("Your zodiac sign is Cancer.")
#         else:
#             print("Your zodiac sign is Gemini.")
#     elif b == "Sep":
#         if a > 22:
#             print("Your zodiac sign is Libra.")
#         else:
#             print("Your zodiac sign is Virgo.")
#     elif b == "Nov":
#         if a > 21:
#             print("Your zodiac sign is Sagittarius.")

#         else:
#             print("Your zodiac sign is Scorpio.")
# else:
#     print("This month does not exist.")

# _________________________________________________________________What is your zodiac sign?(ลอกเพื่อนมา...)

# x = float(input('Enter a price: '))

# if x > 0 :
#     if x < 10000 :
#         print('This TV is cheap.')
#     elif 10000 <= x < 100000 :
#         print('This TV is moderate price.')
#     elif x >= 100000:
#         print('This TV is expensive.')
# else :
#     print('A price must be greater than 0')

# _________________________________________________________________Is this TV cheap, medium price or expensive? 

# a = float(input('Enter A: '))
# b = float(input('Enter B: '))
# c = float(input('Enter C: '))
# ckeck = (b**2)-(4*a*c)
# ans1 = (-b+(ckeck**(1/2)))/(2*a)
# ans2 = (-b-((ckeck**(1/2))))/(2*a)

# if ckeck >= 0 :
#     if ans1 == ans2 :
#         print(f'The answer of this equation is {ans1:.2f}')
#     else :
#         print(f'The answer of this equation is {ans1:.2f} and {ans2:.2f}')
# else :
#     print('The answer of this equation is imaginary number.')

# _________________________________________________________________Quadratic Equation 

# import math
# v = float(input('Enter velocity: '))
# a = float(input('Enter the angle of throwing: '))*math.pi/180
# s = float(input('Enter distance between thrower and the goal: '))

# t = 2*v*(math.sin(a))/9.8
# Sx = v*(math.cos(a))*t
# w = Sx - s
# if w > 0:
#     text = 'the ball go pass the goal.'
# elif w < 0:
#     text = 'the ball can\'t reach the goal.'
# else:
#     text = 'the ball hit the goal perfectly.'

# print(f'The ball can go farthest in x-axis: {Sx:.2f} m and {text}')

# _________________________________________________________________Ball and Goal 







