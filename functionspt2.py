#this example shows default fucntions and how they work.
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function() #note when left empty it will return the default 
my_function("Brazil")

#=---------------------------------------------------------
#using a feeding a list into a function and it remains the same in a function
def myfunc(anime):

    for eachanime in anime:
        print (eachanime)
    
eachanime = ["Bleach" , "Naruto", "DBZ" , "Boruto"]

myfunc(eachanime)


#-----------------------------------------------------------
#if you want a function to return a value
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#--------------------------------------------------------------------
#recursion is when a function calls itself
def tri_recursion(k):
  if(k > 0):
    result = tri_recursion(k - 1) + k
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(10)



#recursion

def fact(n):

    if n == 0:

        return 1

    return n * fact(n-1)

fact(5)

    