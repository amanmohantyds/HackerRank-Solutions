"""
Problem: print 1 to n
Link: https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true

"""
if __name__ == '__main__':
    n = int(input())
    
    for i in range(1,n+1):
        print(i,end='')
        
        
        #Note_1:-
        #end is a parameter of the print() function that tells Python what to print after the output.
        #like:   end='\n' --> where \n means "new line"
        #And:  end=''  --> No new line is added after each print.
        
        #Note_2:-
        #strip() only works on strings, not on a range object
        #range(0, n) creates a range object, and range objects don't have a .strip() method