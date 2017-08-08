#1: Direct way to reverse string without any hassle:

  inputStr = input('Please enter the string for which you want to know the reverse of :').strip()
  #strip method is used to remove trailing an leading spaces

  print(inputStr[::-1])
  
  # We see three parameters while slicing the inputStr.
  #[<firstparameter>:<secondparameter>:<thirdparameter>]
  #First parameter conveys start pos , second parameter conveys stop pos and third parameter conveys the direction and iteration steps
  # when nothing is specified for first parameter and second parameter, thier position depends on the direction in third param(+ or -)
  # if third param is positive then first parameter starts from 0th position and second parameter takes length of string
  # if third param i negative then first parameter takes last position of string and second parameter takes value of None and iteration
  # happens from last to first as in this case
  
  #2: Using Recurrsion to perform the same:
  
    def reverseStr(str):
      if len(str)==1:
          return str
      else:
          return reverseStr(str[1:])+str[0]
    
    reverseStr('hello')
  
