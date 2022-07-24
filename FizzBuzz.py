# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

CurrentNumber = 1

while CurrentNumber <= 100:
    if( CurrentNumber % 15 == 0 ):
        print( "FizzBuzz" )
    elif( CurrentNumber % 3 == 0 ):
        print( "Fizz" )
    elif( CurrentNumber % 5 == 0 ):
        print( "Buzz" )
    else:
        print( CurrentNumber )
    
    CurrentNumber += 1

