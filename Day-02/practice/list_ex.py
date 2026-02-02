a = [100, 200, 300, True, 4.6]  #list banane ka tareeka

print(type(a))      #typecasting to know datatype of a
a.append(500)       #append() is used to add one item to end of list
print(a)            #printing a

clouds = list ()        #list banane ka dusra tarika recommended
print (type(clouds))

clouds.append("aws")
clouds.append("azure")      
clouds.append("gcp")
clouds.append("ibm")
clouds.append("alibaba")
clouds.append("utho")

print(clouds)

print("length of the list is:", len(clouds))

print("world leader for cloud service provider is:",clouds[0])  
#[-1] [2] you can print giving the order number in the list for utho or gcp

print("indian cloud service provide is",clouds[-1])

print(dir(clouds))  #dir function to know what all things you can do with list

print(clouds.extend.__doc__) #extend() adds multiple elements to the list
print(clouds.count.__doc__)  #count() counts how many times an element appear
print(clouds.reverse.__doc__) #reverse() reverses theorder of te list
print(clouds.append.__doc__) #append() adds one element at the endof list

#lets itereate the list

for cloud in clouds:
    if cloud == "aws":
        print(f"{cloud} market leader + covered in course")
    
    elif cloud == "utho":
        print(f"{cloud} Indian Cloud")
    elif cloud == "azure" or "gcp":
        print(f"{cloud} devops zero to hero me covered")
    else:
        print(f"{cloud} baaki nhi honge")
        
# f tells python this is a formatted string
# {cloud} python replaces this with value of the variable in cloud