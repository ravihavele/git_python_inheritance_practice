# # exception handling for devisible by zero error
# a = 12
# b = 5
#
# try:
#     print(a / b)
# except ZeroDivisionError:
#     print('Division by zero not allowed')
# else:
#     print('executed when error not occurred')
# finally:
#     print('executed when error occurred or not')
# print('Do Something')
#
#
# # exception handling for devisible by zero error with Obj message
# a = 12
# b = 0
#
# try:
#     print(a / b)
# except ZeroDivisionError as obj:
#     print(f'Division by zero not allowed /{obj}')
# else:
#     print('executed when error not occurred')
# finally:
#     print('executed when error occurred or not')
# print('Do Something')
#
# # multiple except block
# a = 12
# b = 0
#
# try:
#     print(a / b)
#     # print(a / g)
# except (NameError, ZeroDivisionError) as obj:
#     print(f'Exception/{obj}')
# else:
#     print('executed when error not occurred')
# finally:
#     print('executed when error occurred or not')
# print('Do Something')

#another example for try and except
Num1 = input("Enter Number one: ")
Num2 = input("Enter Number two: ")
try:
    print(f"sum of num1 and num2 is {int(Num1)+int(Num2)}")
except Exception as ex:
    print(ex)
print("This line is important")