#collect string/ test length

#input = input("Please enter an even number: ")
#number = int(input)
#
#if number % 2 == 0:
#    print("Your number is even")
#else:
#    print("Your number is odd")

 

#------------------------------------
#input = input("Please enter test string: ")
#
#if len(input) < 6:
#    print("Too short king")
#    print("Add a few inches")


#----------------------------------------------------
#Using user input to determine if a triangle is scalene, isosceles or equalateral
#Scalene: all sides are different
#Isosceles: 2 sides are equal
#Equalateral: all sides are equal

##x= int(input("length of side a ="))
##y= int(input("length of side b ="))
##z= int(input("length of side c ="))
##
##if x != y and y != z and x != z:
##    print("Scalene")
##elif x == y and y==z :
##    print("Equalateral")
##else:
##    print("Isosceles")
####-----------------------------------------------------------

x = int(input("Please input your age "))
y = int(input("Please input your rounded height "))
z = int(input("Please input your rounded weight in kg ") )

if x > 10<25 and y > 173<187 and z > 68<85 :
    print("young")
elif x > 26  < 50 and y > 173  < 187 and z > 68  < 85 :
    print("middle aged")
elif x > 50  < 80 and y > 150  < 187 and z > 55  < 85 :
    print("old")
else: 
    print("bad metrics")
