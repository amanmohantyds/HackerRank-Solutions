#The provided code stub reads an integer,n, from STDIN. For all non-negative integers i<n , print i square.
#Constraints are 1<=n<=20

if __name__ == '__main__':
    x = int(input())
    
    for i in range(x):
     print(i**2)