"""
Problem: Arithmetic Operator
Link: https://www.hackerrank.com/challenges/python-arithmetic-operators/problem?isFullScreen=true

"""
#Q-->The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:
   #i)The first line contains the sum of the two numbers.
   #ii)The second line contains the difference of the two numbers (first - second).
   #iii)The third line contains the product of the two numbers.
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    sum=a+b
    difference=a-b
    prod=a*b
    print("sum is:",sum)
    print("difference:",difference)
    print("product is:",prod)
