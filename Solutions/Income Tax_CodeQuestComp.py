def round(x, n=0):
    negative = x < 0
    if negative: x *= -1
    x = float(x) * (10 ** n)
    if x % 1 >= 0.5: x+=1
    if negative: x *= -1
    return float(int(x) / 10 ** n)

Testcase = int(input())
for i in range(Testcase):
    MoneyMade = int(input())
    if MoneyMade <= 11000:
        MoneyMade = MoneyMade * 0.10
        MoneyMade = (round(MoneyMade))
        print(MoneyMade.__trunc__())
    elif MoneyMade > 11000 and MoneyMade <= 44725:
        MoneyMade = MoneyMade * 0.12
        MoneyMade = (round(MoneyMade))
        print(MoneyMade.__trunc__())
    elif MoneyMade > 44725 and MoneyMade <= 95375:
        MoneyMade = MoneyMade * 0.22
        MoneyMade = (round(MoneyMade))
        print(MoneyMade.__trunc__())
    elif MoneyMade > 95375 and MoneyMade <= 182100:
        MoneyMade = MoneyMade * 0.24
        MoneyMade = (round(MoneyMade))
        print(MoneyMade.__trunc__())
    elif MoneyMade > 182101 and MoneyMade <= 231250:
        MoneyMade = MoneyMade * 0.32
        MoneyMade = (round(MoneyMade))
        print(MoneyMade.__trunc__())
    elif MoneyMade > 231251 and MoneyMade <= 578125:
        MoneyMade = MoneyMade * 0.35
        MoneyMade = (round(MoneyMade))
        print(MoneyMade.__trunc__())
    elif MoneyMade >= 578126:
        MoneyMade = MoneyMade * 0.37
        MoneyMade = (round(MoneyMade))
        print(MoneyMade.__trunc__())
