user_weight = float(input("enter your weight (kg) : "))

user_height = float(input("enter your height (m) : "))
bmi = user_weight / (user_height * 2) 
print("your bmi is " + str(bmi))



# def bmi(user_weight, user_height):
#  result =  user_weight / user_height ** 2 

# print(bmi(60,1.5))


#function-practice
# onion_price = 30
# carrot_price = 20

# def total_price(onion_count, carrot_count):
#   onion_total_price = onion_price * onion_count
#   carrot_total_price = carrot_price * carrot_count

#   return onion_total_price + carrot_total_price

# print (total_price(2,3))

# def square_area_calculator(a,b):
#   return a * b

# print(square_area_calculator(3,4))