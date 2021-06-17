#write a python script to merge two python dictionaries 
def merge(dict1, dict2): 
       res= {**dict1, **dict2 }
       return res 
dict1={"j":8, "l":7} 
dict2={"h":6, "f":9} 
dict3= merge(dict1,dict2)
print(dict3) 

#write a python program to remove a key from dictionaries 
dict4={"jastin":25, "samuvel":70,"A":20} 
print("Dictionaries before removal :", dict4) 
del dict4["A"] 
print("Dictionaries after removal :",dict4) 

#write a python program to map two list into a dictionaries 
keys=['apple','orange','papaya','grapes'] 
value=['75','85','65','55'] 
fruits=dict(zip(keys,value)) 
print(" mapping two list into dictionaries :",fruits) 

#write a python program to find the length of the set 
j =len({"11","21","32","43","54"})
print("The length of the set is :",j) 

#writs a python program to remove the intersection of 2nd set from 1st set 
set1={'1','5','9','6','7'} 
set2={'9','3','2','5','4'} 
print("Current set :") 
print(set1) 
print(set2) 
print("\n remove the intersection of 2nd set from 1 st set using -= operator :") 
set1 -= set2 
print("set1",set1) 
print("set2",set2)