
# exercise 1
d1 = {'a': 15, 'b': 20}
d2 = {'x': 25, 'y': 30}
d = d1.copy()
d.update(d2)
print(d)

# exercise 2

my_list = ["2","4","1","5","3"]
my_list.sort()
print (my_list) #in ascending order
my_list.sort(reverse=True)
print (my_list) #in descending order

my_set = set = set(my_list)
print (my_set) #list into set conversion

# exercise 3
# function to list and sort the number of items

dictionary = {"key1":3,"key2":1,"key3":2}
def alpha(my_dictionary):
    print (my_dictionary.keys())
    
alpha (dictionary)

print ("\n")

# without function

count = 0
for x in dictionary: 
    if isinstance(dictionary[x], list): 
        count += len(dictionary[x]) 
    print(x)

# exercise 4

string_1 = " Hi World"
print(string_1)

def search_and_replace(x):
    a=input("enter the word to search: ")
    b=input("enter the word to replace: ")
    print (x.replace(a,b,1))
    
search_and_replace(string_1)

# exercise 5

string_2 = " i am dani"
print (string_2)

def capitalise(y):
    c = input ("enter the word to be find: ")
    result = c.capitalize()
    print(y.replace(c,result))
    
capitalise(string_2)

# exercise 6

list_1 = ["one","two","two","three","four","five","five"]

def find_repeats(z):
    ans = dict((i, z.count(i)) for i in z)
    print (ans)

find_repeats(list_1)

# exercise 7

print ("enter three value to be added")
l =int(input("operand_1="))
m =int(input ("operand_2="))
n =int(input ("operand_3="))
addition=l+m+n
print ("operand_1+operand_2+operand_3 =",addition)
divisor=int(input("enter the divisor="))
answer= addition/divisor
print ("your final answer is",answer)

# exercise 8

num_1=int(input("operand_1="))
num_2=int(input("operand_2="))
num_3=int(input("operand_3="))
mean=(num_1+num_2+num_3)/3
print ("mean is ", mean)
median = [num_1,num_2,num_3]
median.sort()
print ("median is ",median[1])
print ("mode is ", median[2])

# exercise 9

string_x="this is a demo class"
print (string_x)
print(string_x.swapcase())

# exercise 10

def DecimalToBinary(num):
    if num >= 1:
        DecimalToBinary(num // 2)
        print (num % 2)
        
DecimalToBinary(68)