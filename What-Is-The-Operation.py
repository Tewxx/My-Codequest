Testcase = int(input())
for i in range(Testcase):
    FirstOpperator, SecondOpperator, Answer = input().split(" ")
    if int(FirstOpperator) + int(SecondOpperator) == int(Answer):
        print("Addition")
    elif int(FirstOpperator) - int(SecondOpperator) == int(Answer):
        print("Subtraction")
    elif int(FirstOpperator) * int(SecondOpperator) == int(Answer):
        print("Multiplication")
    elif int(FirstOpperator) // int(SecondOpperator) == int(Answer):
        print("Division")
    else:
        print("Modulo")