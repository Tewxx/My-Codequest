Testcase = int(input())
for i in range(Testcase):
    Numpy = list(map(int, input().split(" ")))
    Numpy.sort()
    print(max(Numpy))
