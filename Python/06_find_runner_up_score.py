if __name__ == '__main__':
    print("Enter number of scores:")
    n = int(input())
    print("Enter scores")
    arr = map(int, input().split())
    scores= list(arr)
    print("runner up score is:",sorted(set(scores))[-2])







                                   # CONCEPT OF QUESTION

#Note:- " set() " can be used to remove the duplicates
    #Example:- scores=[2,4,5,3,3,1,1,2]  --> set(scores) --> [2,4,5,3,1]
    
#Note:-
    #To store items in a list use --> list()   
    
        
#You should use sorted() instead of .sort() when you need to preserve the original 
                      #order of your data or when you are sorting data types other than lists 
                      
#To access the last item [-ve]    ,example:- b=["apple", "banana", "cherry"]
                                              #print(b[-1]) #prints --> cherry  
                                              
                                              #So, for second last item use x[-2] 
                                              

 

    #First line: n
         #This tells us how many numbers are coming.  
    #Second line: scores
         # 2 3 6 6 5
         #Python reads this as one string
         #We need to split it into individual numbers.
    
    #THATS WHY Use input().split()
    #If number is 2 3 6 6 5
             #after input().split()
    #['2', '3', '6', '6', '5']

#To convert them into integers: use map()   
     #map(int, input().split())
     #2, 3, 6, 6, 5
         
                                                                           
#Then To store them in a list: use list()
#Then use set() to remove the duplicated
#Then use sorted() to sort everything
