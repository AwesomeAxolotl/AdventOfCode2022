import re
from copy import deepcopy

with open("input5.txt", "r") as f:
    d = [x.strip("\n") for x in f.readlines()]
    
    # part 1
    
    i = 0
    stackLevels = []
    while "[" in d[i]:
        stackLevels.append(list(re.findall(r"    ?|\[([A-Z])\] ?", d[i])))
        i += 1
    
    stacks = [[] for _ in stackLevels[0]]
    
    for level in reversed(stackLevels):
        for pos, value in enumerate(level):
            if value != "":
                stacks[pos].append(value)
    
    i += 2
    p2stacks = deepcopy(stacks)
    
    while i < len(d):
        command = [int(x) for x in re.findall("[0-9]+", d[i])]
        for _ in range(command[0]):
            stacks[command[2]-1].append(stacks[command[1]-1].pop())
        
        # part 2
        p2stacks[command[2]-1].extend(p2stacks[command[1]-1][-command[0]:])
        p2stacks[command[1]-1] = p2stacks[command[1]-1][:-command[0]]
        i += 1
    
    print("".join([x[-1] for x in stacks]))
    print("".join([x[-1] for x in p2stacks]))