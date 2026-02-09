#No.1
def fizzbuzz_plus(n):
    for x in range(n):
        if x % 3 & 5 == 0:
            print ("FizzBuzz")
    
        elif x % 3 == 0:
            print ("Fizz")
    
        elif x % 5 == 0:
            print ("Buzz")

        elif x % 7 == 0:
            print ("Seven")
        
        else:
            return x
        
print (fizzbuzz_plus(21))



