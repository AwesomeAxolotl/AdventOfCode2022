import re

with open("input3.txt", "r") as f:
    d = [x.rstrip() for x in f.readlines()]
    
    # part 1
    # a-z 1-26, ascii a = 97 -> -96
    # A-Z 27-52 ascii A = 65 -> -38
    
    prioritySum = 0
    
    for items in d:
        firstHalf = items[:int(len(items)/2)]
        secondHalf = items[int(len(items)/2):]
        identical = re.search(f"[{firstHalf}]", secondHalf)[0]
        ascii = ord(identical)
        prioritySum += ascii - 96 if ascii >= 97 else ascii - 38
    
    print(prioritySum)
    
    # part 2
    
    badgeSum = 0
    
    for i in range(int(len(d)/3)):
        results = re.findall(f"[{d[i*3]}]", d[i*3+1])
        matches_1_2 = "".join(results)
        badge = re.search(f"[{matches_1_2}]", d[i*3+2])[0]
        ascii = ord(badge)
        badgeSum += ascii - 96 if ascii >= 97 else ascii - 38
    
    print(badgeSum)