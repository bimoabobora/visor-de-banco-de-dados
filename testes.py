var = 0
def test():
    global var
    var += 1

    print(var)

for _ in range(5):
    test()
