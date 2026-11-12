def reverseName(s):
    n = len(s) #for Ali is n = 3
    res = ""
    for i in range(n-1, -1, -1):
        print(s[i])
        res = res + s[i]

    print(res)
        

print(reverseName("zohaib"))