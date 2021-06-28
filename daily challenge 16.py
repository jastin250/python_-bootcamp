#To create a lambda function that multiplies argument x with argument y 

l = lambda x,y : x*y 
print(l(20,5)) 

#Write a Python program to create Fibonacci series to n using Lambda 

from functools import reduce 

f = lambda n: reduce(lambda q, _: q+[q[-1]+q[-2]],
                                range(n-2), [0, 1]) 
print(f(20)) 

#Write a Python program that multiply each number of given list with a given number 

numbers = [11,22,33,44,55] 
n = int(input("enter a number")) 
print("original list :",numbers) 
print("given number :",n) 
filtered_numbers=list(map(lambda number:number*n,numbers))
print("Result:")
print(' '.join(map(str,filtered_numbers))) 

#Write a Python program to find numbers divisible by 9 from a list of numbers 

L = [8,9,5,27,46,64,90] 
res = list(filter(lambda q: (q% 9 == 0), L))
print("Numbers divisible by 9 is",res) 


#To count the even numbers in a given list of integers 
L1 = [2,4,5,8,6,9,3,22,55]  
even_number = list(filter(lambda q: (q% 2 == 0), L1)) 
print("Even numbers in the list are: ", even_number)  