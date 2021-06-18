#create a function getting two integer inputs from the user and print the following 
def my_function(a,b):
	  print("sum of a and b :", a+b) # addition 
	  print("subtraction of a and b :", a-b) #subtraction 
	  print("division of a and b :", a/b) #division 
	  print("multiplication of a and b :", a*b)# multiplication 
my_function(a=int(input("Enter the first number :")), b=int(input("Enter the second num er :")))  


#create a function name covid it should accept patient name and body temperature by default the body temp is 98 degree 

def covid(patientname, bodytemperature):
	print("Patient Details: ")
	print("Patient  name : " , patientname)
	print("Default temperature : 98 degree ") 
	print("patient body temperature :",bodytemperature ,"degree")
covid(patientname=str(input("Enter the Patient name : ")), bodytemperature=int(input("Enter the Patient body temperature in degree : ")))


     