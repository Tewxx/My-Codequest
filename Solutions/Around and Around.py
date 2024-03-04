def round(x, n=0):
    negative = x < 0
    if negative: x *= -1
    x = float(x) * (10 ** n)
    if x % 1 >= 0.5: x+=1
    if negative: x *= -1
    return float(int(x) / 10 ** n)

TestCase = int(input())
for i in range (TestCase):
    MyLittleInput = int(input())
    Circfimunce = 40075
    Circfimunce = Circfimunce/6.283185308 # pi * 2 earths raidus
    Circfimunce = Circfimunce + MyLittleInput
    Circfimunce = 2*3.141592654*Circfimunce
    print(f"{Circfimunce:.1f}")
