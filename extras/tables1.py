def tables1(n):
    maxnum = str(n*n)
    max_spaces = len(maxnum)

    for i in range(1, n+1):
        for j in range(1, n+1):
            if j == 2:
                print ("|",end = "")
            if j >= 2:
                print(" " * (max_spaces - len(str(i*j))),end = "")
            print(f"{i*j}", end = " " )
        print("\n")
        if i == 1:
            print(" --+",end = "")
            print("---" * (n-1))
tables1(10)
