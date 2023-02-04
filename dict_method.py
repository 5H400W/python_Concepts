my_dict = {
    "Fast" : "faster" ,
    "name" : "prashant",
    "makes": "food",
    "place" : "India",
    "marks":[1,2,5,8,9,7,6,4]
    
}

"""
dictionary is non ordered
dict is mutable
dict is indexed
dict cant have same keys
"""

print(my_dict)

print(my_dict.values())

print(my_dict.keys())

print(my_dict.items)


print(my_dict)
#update the dict values and add using update function 


update_dict= {
    "name":"pashant Dwivedi",
    "marks": [54,85,78,960],
    "Place":"lucknow,India",
    "exp": 1,
    450:45   
}
my_dict.update(update_dict)
print(my_dict)


print(my_dict["exp"])