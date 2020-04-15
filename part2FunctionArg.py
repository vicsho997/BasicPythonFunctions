import sys; #x = 'foo'; sys.stdout.write(x)
import time as tm
import calendar as cal

#f(x), defining a function, def function(paramters):
def printMe1(str):
    str = "This prints a passed string into this function"
    print(str)
    return

"""Function Args- Required Args, Keyword Args, Default Args, Variable-length Args, Anonymous f(x)"""
    
    #Required Args - Args passed to a f(x) in correct positional order
        #Number of Args in the f(x) call, should match exactly with f(x) def
def printMe2(str):
    str = "This prints a passed str into this f(x)"
    print(str)
    return        

    #Keyword Args - caller identifies the Arg by the parameter of name
        #Skip Arg or place out of order because interpreter can use keywords to match the values with parameters
            #One Arg
def printMe3(str):
    print (str)
    return
#now you can call printMe3 f(x)
printMe3(str = "My String")
print('\n')       
             #Two Args 
def printInfo1(name, age):
    print("Name:", name)
    print("Age:", age)
    return
#can call printInfo
printInfo(age = 50, name = "Miki")
print('\n') 

    #Default Args- assume default value if value is not provided in f(x) call for that arg
def printInfo2(name, age = 35):
    print("Name:", name)
    print("Age:", age)
    return

printInfo2(age = 50, name = 'miki')
printInfo2(name = 'niki')
print('\n') 

    #Variable-length Args - to process f(x) for more args than specefied when def the f(x)
        #syntax for non-keyword variable arbs is below def f(x) name
            #def f(x): ([formal_args,]*var_args_tuple):
        #an asterick (*) is placed before variable name that holds the value of all non-keyword variable args.
            #the tuple is empty if no additional args are specefically in call
def printInfo3(arg1,*vartuple):
    print(arg1)
    for var in vartuple:
        print (var)
        return
     
printInfo3(10)
printInfo3(70,60,50)
print('\n') 


    #Anonymous f(x)-use lambda keyword to create small anonymous f(x) lambda (arg1):
        #can take many args, but only return one value in form of expression
        #cannot be direct call to print, lambda needs expression
        # https://www.w3schools.com/python/python_lambda.asp
    #V1
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) 
print(mytripler(11))
   
  
