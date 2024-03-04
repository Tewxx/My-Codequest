Testcase = int(input())
for i in range (Testcase): # Below you have to turn weight into the amount of cans
    WeightOfRecycledCans, WeightOfRecycledPlastic, WeightOfRecycledGlass = input().split()
    WeightOfRecycledCans = int(WeightOfRecycledCans) / 0.03225806451
    WeightOfRecycledPlastic = int(WeightOfRecycledPlastic) / 0.06666666666
    WeightOfRecycledGlass = int(WeightOfRecycledGlass) / 2 
    RecycledCans = WeightOfRecycledCans * 0.05
    RecycledPlastic = WeightOfRecycledPlastic * 0.10
    RecycledGlass = WeightOfRecycledGlass * 0.20
    Total = float(RecycledGlass) + float(RecycledPlastic) + float(RecycledCans)
    Total = (f"{Total:.2f}")
    Total = str(Total)
    print("$"+Total)
