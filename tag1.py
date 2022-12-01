with open("input1.txt", "r") as f:
    d = [x.rstrip() for x in f.readlines()]
    
    # part 1
    elves = []
    cur = 0
    for kcal in d:
        if kcal == "":
            elves.append(cur)
            cur = 0
        else:
            cur += int(kcal)
    if cur > 0:
        elves.append(cur)
    print(max(elves))
    
    # part 2
    elves.sort(reverse = True)
    print(sum(elves[0:3]))