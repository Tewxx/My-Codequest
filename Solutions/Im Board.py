TestCase = int(input())
for i in range (TestCase):
    SizeBoard = int(input())
    (ActualBoard) = str()
    for i in range (SizeBoard):
        ActualBoard = (ActualBoard + "# ")
    for i in range (SizeBoard):
        print(ActualBoard.strip())
