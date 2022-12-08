import re

with open("input4.txt", "r") as f:
    d = [x.rstrip() for x in f.readlines()]
    
    # part 1 & 2
    
    contained = 0
    noOverlaps = 0
    
    for assigns in d:
        fromTo = [int(x) for x in list(re.findall("[0-9]+", assigns))]  
        if (fromTo[0] >= fromTo[2] and fromTo[1] <= fromTo[3]) or (fromTo[2] >= fromTo[0] and fromTo[3] <= fromTo[1]):
            contained += 1
        if (fromTo[1] < fromTo[2]) or (fromTo[3] < fromTo[0]):
            noOverlaps += 1
            
    print(contained)
    print(len(d)-noOverlaps)
    