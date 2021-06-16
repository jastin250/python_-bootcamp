#create list of integer 
num_list = [1,2,3,4,5,6,7,8,9,10] 
print("list is :", num_list) 
#add an item into the list 
num_list.append(200) 
print("list after appending a value is",num_list) 
#delete an item  
num_list=[1,2,3,4,5,6,7,8,9,10]
a=num_list.pop(2) 
print("item poped:",a) 
print("after deleting the item",num_list) 
#store the largest number from the list to variable
num_list=[1,2,3,4,5,6,7,8,9,10]
print("a:",max(num_list)) 
#store the smallest number from the list to variable 
print("b:",min(num_list)) 

#sum2 
#create a tuple and print the reverse of the tuple 
def reverse(tuples) :
    new_tup=tuples[::-1] 
    return new_tup
tuples =('20','21','22','23','24','25')
print("reverse of created tubles:",reverse(tuples))
  

#sum3 
#create a tuple and convert tuple to list 
Tup1 = (1,"abc",2.3,'d')  
list = list(Tup1)
print("tuble converted to list :",list)