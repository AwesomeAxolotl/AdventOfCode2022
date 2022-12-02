with open("input2.txt", "r") as f:
    d = [x.rstrip() for x in f.readlines()]
    
    # part 1
    # AX rock 1pt
    # BY paper 2pt
    # CZ scissors 3pt
    scenarios = {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6}
    points = 0
    for play in d:
        points += scenarios[play]
    print(points)
    
    # part 2
    # X = pick to lose
    # Y = pick to draw
    # Z = pick to win
    
    conversion = {"A X": "A Z", "A Y": "A X", "A Z": "A Y", "B X": "B X", "B Y": "B Y", 
                  "B Z": "B Z", "C X": "C Y", "C Y": "C Z", "C Z": "C X"}
    points = 0
    for play in d:
        points += scenarios[conversion[play]]
    print(points)