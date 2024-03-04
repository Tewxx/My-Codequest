TestCase = int(input())
for i in range (TestCase):
    GorrillaFight = input()
    if GorrillaFight == ("true false"):
        print("false")
    elif GorrillaFight == ("false true"):
        print("false")
    elif GorrillaFight == ("true true"):
        print("true")
    elif GorrillaFight == ("false false"):
        print("true")