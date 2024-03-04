Testcase = int(input())
for i in range (Testcase):
    Setence = input()
    Words = Setence.split(" ")
    for i in range (len(Words)):
        if Words[i] == "Nimo":
            print(i+1)
        else:
            print("Nimo was not found")
