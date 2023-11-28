# print "Fizz" instead of a number divisible by 3.
# print "Buzz" instead of a number divisible by 5.
# print "FizzBuzz" instead of a number divisible by both 3 and 5.
# Otherwise, say the number as it is.


number = int(input("let's fizz buzz game! enter any number : "))

def fuzzbuzz(number):
  for num in range(1, number + 1):
    if num % 3 == 0 and num % 5 == 0:
      print( "FizzBuzz") 
    elif num % 3 == 0:
      print( "Fizz")
    elif num % 5 == 0:
      print( "Buzz")
   
    else:
      print(num)
      
fuzzbuzz(number)

