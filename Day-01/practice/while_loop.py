num = int(input("enter the number you want the table for"))

name = input("enter dost ka name")
print(f"hello dosto,{name}")

for i in range (1,11):
    print(f"{num} * {i} = {num*i}")

suraj = "chand"

while suraj == "chand":
    print("prathamesh")  #infinite loop
    break

choice = input("enter the choice(press q to quit):")

while choice != "q":
    num = int(input("enter the number you want the table for"))
    
    for i in range (1,11):
        print(f"{num} * {i} = {num*i}")
    choice = input("enter the choice(press q to quit):")