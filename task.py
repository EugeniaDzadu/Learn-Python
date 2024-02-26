# age = []
# for i in range(10):
#  ages = int(input('Enter age: '))
#  age.append(ages)
#  print(age)

# age = range(10)
# print(list(age))

# Number 1
# sum = 0
# for i in range(10):
#     num = int(input('Enter numbers: '))
#     sum = sum+num
# print(sum)

# Number 2
# even_num=[]
# for i in range(10):
#     num = int(input('Enter the numbers: '))
#     if num%2 == 0:
#         even_num.append(num)
# print(even_num)

# Number 3
firstname = input('Enter first name: ')
lastname = input('Enter last name: ')
age = int(input('Enter age: '))
print(firstname, lastname, age)
if age >= 18:
    print(f"{firstname} {lastname} {age} you are eligible to vote")
else:
    print(f"{firstname} {lastname} {age} you are not eligible to vote")