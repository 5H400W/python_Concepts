#find given  number is pime or not 

num = int(input("enter the number \n")) #take input from user

prime = True # set prime as true

#start for loop
for i in range(2,num):
    if(num%i==0 ):
        prime = False
        break
if prime:
    print("yes number is prime")
else:
    print("number is not pime")        

