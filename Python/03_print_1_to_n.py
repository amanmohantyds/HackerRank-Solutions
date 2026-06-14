print("Print a function using for loop without using range")

#Print a function
#Q)The included code stub will read an integer,n, from STDIN. Without using any string methods, 
                                                                 # try to print the following: 1,2,3,

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