with open("input6.txt", "r") as f:
    d = f.read().rstrip()
    
    last = {}
    c = 0
    #delay = 4 # part 1
    delay = 14 #part 2
    duplicates = 0
    
    while True:
        if d[c] in last:
            if last[d[c]] > 0: duplicates += 1
            last[d[c]] += 1
        else:
            last[d[c]] = 1
        if c >= delay:
            if last[d[c-delay]] > 1: duplicates -= 1
            last[d[c-delay]] -= 1
        
        if c >= delay-1:
            if duplicates == 0:
                break
        c += 1
    
    print(c+1)