# Example Code 1

def say_hi(): #defining the function say_hi()
  print("Why hello there!") #when the function say_hi() is called, the computer would run this line of code which is printing "Why hello there!" on the console. 

def offer_drink():#defining the function offer_drink()
  print("Would you care for a spot of tea?") #when the function offer_drink() is called, the computer would run this line of code which is printing "Would you care for a spot of tea?" on the console.

def offer_food():#defining the function offer_food()
  print("Biscuit?")#when the function offer_food() is called, the computer would run this line of code which is printing "Biscuit?" on the console.

def say_bye():#defining the function say_bye()
  print("Cheerio then.")#when the function say_bye() is called, the computer would run this line of code which is printing "Cheerio then." on the console.


offer_drink()#Calling the function offer_drink, which will run the code inside the function. The computer will print "Would you care for a spot of tea?" on the console.
say_hi()#Calling the function say_hi, which will run the code inside the function. The computer will print "Why hello there!" on the console.
offer_food()#Calling the function offer_food, which will run the code inside the function. The computer will print "Biscuit".

# Example code 2
def maths1(): #defining the function maths1()
  num1 = 50 #assigning the number value 50 to the variable num1
  num2 = 5 #assigning the number value 5 to the variable num2
  return num1 + num2 #returning the value of the sum of num1 + num2 which is 55

def maths2():#defining the function maths2()
  num1 = 50#assigning the number value 50 to the variable num1
  num2 = 5#assigning the number value 5 to the variable num2
  return num1 - num2 #returning the value of the sum of num1 - num2 which is 45

def maths3():#defining the function maths3()
  num1 = 50 #assigning the number value 50 to the variable num1
  num2 = 5 #assigning the number value 5 to the variable num2
  num2 = 5#assigning the number value 5 to the variable num2
  return num1 * num2 #returning the value of the sum of num1 * num2 which is 250

outputNum = maths2() #assigning the value of the function maths2() to the variable outputNum
print(outputNum) #print the value of the variable outputNum which is 45

# Example Code 3
def location(country): #defining the function location with a parameter of country
  print("I am from " + country) #When the function is called the output will be "I am from" + the value of the parameter country


location("Brazil") # the parameter of Brazil so the output will be "I am from Brazil"

