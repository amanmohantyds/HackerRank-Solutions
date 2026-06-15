
                                           CONCEPTS OF LISTS 
-> To change list item use x[n]

-> Change a Range of Item Values with [x:y]

-> .append() :add items at last
                           #st = ["apple", "banana", "cherry"]
                              # st.append("orange")
-> .insert() :add items at specific index using (index,item)
                                #thislist = ["apple", "banana", "cherry"]
                                  # thislist.insert(1, "orange")
-> .extend() :add elements from another list to the current list  

-> The .extend() is not same as .append()
       # In extend() you can add any iterable object (tuples, sets, dictionaries etc)             

-> remove()
         #y=["Hi,","Welcome","to","candy","town"]
           # y.remove("Hi,")   

-> pop() method: removes the specified index,example x.pop(1) remove second item and if nothing 
                                                                                 # mentioned x.pop()
                                # use integer index or empty for last item   
                                    
-> del keyword: also removes the specified index and it uses "[] symbol to specify index"     
             #del keyword: also delete the list completely
             #Example below:-
             # k = ["apple", "banana", "cherry"]
             # del k[0]  --> deletes apple
             # del k  --> deletes entire k

-> .clear() method empties the list


#Note:- " set() " can be used to remove the duplicates
    #Example:- scores=[2,4,5,3,3,1,1,2]  --> set(scores) --> [2,4,5,3,1]
    
#Note:-
    #To store items in a list use --> list()   
    
        
-> You should use sorted() instead of .sort() when you need to preserve the original 
                      #order of your data or when you are sorting data types other than lists 
                      
-> To access the last item [-ve]    ,example:- b=["apple", "banana", "cherry"]
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


## Finding the runner-up score
- Use set(arr) to remove duplicate scores
- sorted(set(arr)) sorts unique values ascending
- sorted(set(arr))[-2] gives the second-highest (runner-up)
- Example: sorted(set([2, 3, 6, 6, 5]))[-2] -> 5



 

 