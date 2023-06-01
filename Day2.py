#---Part 1---

input =         {'A': 'Rock',
                 'X': 'Rock',
                 'B': 'Paper',
                 'Y': 'Paper',
                 'C': 'Scissors',
                 'Z': 'Scissors'}

pointsShape =   {'Rock': 1,
                'Paper': 2,
                'Scissors': 3}

pointsOutcome = {'Lose': 0,
                 'Draw': 3,
                 'Win': 6}

totalScore = 0

with open('2022/Input/Day2.txt') as f:
    lines = f.readlines()
    rounds = [entry.strip() for entry in lines]

    for round in rounds:
        opponentShape = input[round[0]]
        myShape = input[round[2]]

        if opponentShape == myShape:
            totalScore += (pointsOutcome['Draw'] + pointsShape[myShape])
        elif (opponentShape, myShape) in [('Paper', 'Rock'), ('Rock', 'Scissors'), ('Scissors', 'Paper')]:
            totalScore += (pointsOutcome['Lose'] + pointsShape[myShape])   
        else:
            totalScore += (pointsOutcome['Win'] + pointsShape[myShape])

    print('Your total score is: ')
    print(totalScore)