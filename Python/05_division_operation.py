print("Division Operation")

#Q->The provided code stub reads two integers, a and b, from STDIN.
 # Add logic to print two lines. The first line should contain the result of integer division, a//b .
 # The second line should contain the result of float division, a/b.
if __name__ == '__main__':
    print("enter a:")
    a = int(input())
    print("enter b:")
    b = int(input())
    
    integerDivision=a//b
    floatDivision=a/b
    
    print("integerDivision od a and b:",integerDivision)
    print("floatDivision of a and b:",floatDivision)