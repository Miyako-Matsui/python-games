weight = int(input("Weight: "))
unit = input(("(K)g or (L)bs: "))
if unit.upper() == "K":
   converted = weight / 0.45
   print("K",converted)
else:
   converted = weight * 0.45
   print("L", weight)


# float(weight * 0.45)
# int(weight * 2)
# birth_year = input("enter your birth year: ")
# age = 2020 - int(birth_year)
# print(age)

# int()
# float()
# bool()
# str()

# first_number = float(input("First: "))
# second_number = float(input("Second: ")) 
# sum = first_number + second_number
# print("Sum "+ str(sum))

# name = "John Smith"
# age = 20 
# patient_history = "new"

# print("Name : " + name + " Age : " + str(age) + " Patient Histry :" + patient_history) 
