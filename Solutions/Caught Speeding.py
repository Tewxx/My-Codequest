Testcase = int(input())
for i in range (Testcase):
    Speed, Birthday = input().split(" ")
    if int(Speed) <= 60 and Birthday == "false":
        print("no ticket")
    elif int(Speed) <= 65 and Birthday == "true":
        print("no ticket")
    elif int(Speed) >= 61 and int(Speed) <= 80 and Birthday == "false":
        print("small ticket")
    elif int(Speed) >= 66 and int(Speed) <= 85 and Birthday == "true":
        print("small ticket")
    else:
        print("big ticket")
