def round(x, n=0):
    negative = x < 0
    if negative: x *= -1
    x = float(x) * (10 ** n)
    if x % 1 >= 0.5: x+=1
    if negative: x *= -1
    return float(int(x) / 10 ** n)

TestCase = int(input())
for i in range (TestCase):
    UnSplitMoney = input()
    Split = UnSplitMoney.replace("$", "", 1)
    Split = float(Split)
    FiftenPercent = Split * 0.15
    FiftenPercent = round(FiftenPercent,2)
    EightteenPercent = Split * 0.18
    EightteenPercent = round(EightteenPercent,2)
    TwentyPercent = Split * 0.20
    TwentyPercent = round(TwentyPercent, 2)
    print("Total of the bill:",UnSplitMoney)
    print(f"15% = ${FiftenPercent:.2f}")
    print(f"18% = ${EightteenPercent:.2f}")
    print(f"20% = ${TwentyPercent:.2f}")

