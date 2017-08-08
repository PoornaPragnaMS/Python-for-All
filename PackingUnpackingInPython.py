##In this program we are going to see iterables in python and how we can pack and unpack them

#1: Let us consider a primitve iterable data type as our first case: String

    #Request an input string from End User and use strip function to remove trailing and leading spaces around the string

    inputStr = input("Enter your input to unpack it :").strip() #Assume the input entered is "Hello"

    print(inputStr,sep=",") # printing without unpacking the string, Response here is "Hello"
    print(*inputStr,sep=",") #printing after unpacking the string, Response here is "H,e,l,l,o" due to iterable property of string

#2: Let us consider the second iterable type List for unpacking operation

    inputList = ["Mango","Orange","Apple"]
    print(*inputList)

#3: Unpacking the range function

    print(*range(10), sep = ",") #prints 0,1,2,3,4,5,6,7,8,9

#4: Packing the input parameter of a function and passing tupple as an argument to the function

    Total = 0
    def summation(*numbers):
        for number in numbers:
            global Total
            Total+=number
        print(Total) 

    summation(0,10,20,30) # we must see the result as 60
    


