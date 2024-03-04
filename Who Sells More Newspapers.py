Testcase = int(input())
for i in range (Testcase): 
    Times, Herald = input().split(" ")
    if int(Times) == int(Herald):
        print("Times and Herald have the same number of subscribers")
    elif int(Times) > int(Herald):
        BungeyCoord = int(Times) - int(Herald)
        print("Times has " + str(BungeyCoord) + " more subscribers")
    else:
        BungeyCoord = int(Herald) - int(Times)
        print("Herald has " + str(BungeyCoord) + " more subscribers")
