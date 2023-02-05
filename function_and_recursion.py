# #inserting a default parameter value  in function
# def greet(name = "strangerr"): 
#     print("Good day ahead: ",name)
    
# greet("pD")

"""
Recursion: is function which call itself

"""
#finding factorial using iterative method
# def facto_iter(n):
#     product =1
#     for i in range(n):
#         product=product*(i+1)
#     print (product)

# print(facto_iter(5))

#create a program to find factorial of number using ecursion


def fact_rec(num): #factoial using recursiv 
    if num==1 or num==0:
        return 1
    return num * fact_rec(num -1)


print(fact_rec(0))
