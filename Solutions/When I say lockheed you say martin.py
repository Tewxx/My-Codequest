Testcase = int(input())
for i in range (Testcase):
    UserSays = int(input())
    if UserSays%3==0 and UserSays%7==0:
        print("LOCKHEEDMARTIN")
    elif UserSays%7==0:
        print("MARTIN")
    elif UserSays%3==0:
        print("LOCKHEED")
    else:
        print(UserSays)

    
        
