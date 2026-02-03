info = {
    "name" : "Shubham Bhaiya", #str
    "city" : "Pune", #str
    "qualification": "Mtech", #str
    "age" : 29, # int
    "salary": 22.5, # float
    "married": True, # Bool
    "favourites" : ["teaching", "movies", 18]
}

print("I live in",info["city"]) #print using info wiith key inside []
                                #you put key and you get value printed
                                
print("I love ", info.get("favourite","Not Found")) #get function is safer
                #it wont crash if the key doesnt exist and return none or default printed

info.update({"channel": "TrainWithShubham"}) #if you want to insert anything in dictionary use update()
print(info)
                        #we cant append() in dict
print(info.get,__doc__)                        
print(dir(info))    #to check what all function dict can perform

#iterate dict

for i in info:
    print (i) # you will only get keys printed

for key,value in info.items(): #items() will print both key and value
                                #check print(dir(info)) to know items()
    print(key,value)        # now you will get key&values (items)printed