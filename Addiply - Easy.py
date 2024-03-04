TestCase = int(input())
for i in range(TestCase):
    Number1, Number2 = map(int, input().split())
    Added = Number1 + Number2
    Muliplied = Number1 * Number2
    print(Added, Muliplied)
