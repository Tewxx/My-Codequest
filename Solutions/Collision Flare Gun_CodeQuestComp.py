Testcase = int(input())
for i in range(Testcase):
    Numbers = input()
    Numbers = Numbers.split(",")
    V1 = float(Numbers[0])
    M1 = float(Numbers[1])
    V2 = float(Numbers[2])
    M2 = float(Numbers[3])
    Firststep = M1*V1
    Secondstep = M2*V2
    ThirdStep = Firststep + Secondstep
    ForthStep = M1 + M2
    FinalAnswer = ThirdStep/ForthStep
    print(f"{FinalAnswer:.2f}")
