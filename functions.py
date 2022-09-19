#functions
def name(f_name): #you can put an arg in the () after you name the function
    print(f_name + " Clegg")


name("John")
name("James")
name("Jane")

#--------------------------------------------------------------------------------
#functions
def name(f_name, l_name): #you can put an arg in the (parameter) after you name the function
    print(f_name + " " + l_name)


name("John", "Clegg")
name("James", "Clegg")
name("Jane", "Clegg")

#---------------------------------------------------------------------------------
#3 arguments
#functions
def name(f_name, m_name, l_name): #you can put an arg in the () after you name the function
    print(f_name + " " + m_name + " " + l_name)


name("John", "William", "Clegg")
name("James","Philip",  "Clegg")
name("Jane", "Elizabebth" ,"Clegg")
#---------------------------------------------------------------------------------
#using an astrix gives access to a tuple of arguments, if no. of argumnets is unknown
#functions
def my_function(*anime):
  print("The youngest child is " + anime[2])

my_function("OP", "NRO", "BCH")

#-----------------------------------------------------------------------------------

def name(f_name, m_name, l_name): #you can put an arg in the () after you name the function
    print("My last name is " + l_name)

name(f_name = "John", m_name="William" , l_name="Clegg")





