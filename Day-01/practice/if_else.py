env = input("enter the environment")

print("the user input env is:", env)

#if env == "prod":
    #print("dont deploy on friday")
#else:
    #print("safe to deploy any day")

if env =="prod":
    print("dont deploy on friday")
elif env =="stage":
    print("take backup and test very well")
elif env =="uat":
    print("can test anytime")
elif env =="sit":
    print("test on monday")
