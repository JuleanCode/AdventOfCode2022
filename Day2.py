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

totalScorePart1= 0

with open('2022/Input/Day2.txt') as f:
    lines = f.readlines()
    rounds = [entry.strip() for entry in lines]

    for round in rounds:
        opponentShape = input[round[0]]
        myShape = input[round[2]]

        if opponentShape == myShape:
            totalScorePart1 += (pointsOutcome['Draw'] + pointsShape[myShape])
        elif (opponentShape, myShape) in [('Paper', 'Rock'), ('Rock', 'Scissors'), ('Scissors', 'Paper')]:
            totalScorePart1 += (pointsOutcome['Lose'] + pointsShape[myShape])   
        else:
            totalScorePart1 += (pointsOutcome['Win'] + pointsShape[myShape])

    print('Your total score is: ')
    print(totalScorePart1)

#---Part 2---

input =         {'A': 'Rock', 
                 'B': 'Paper', 
                 'C': 'Scissors', 
                 'X': 'Lose', 
                 'Y': 'Draw', 
                 'Z': 'Win'}

pointsShape =   {'Rock': 1,
                'Paper': 2,
                'Scissors': 3}

pointsOutcome = {'Lose': 0,
                 'Draw': 3,
                 'Win': 6}

totalScorePart2= 0

with open('2022/Input/Day2.txt') as f:
    lines = f.readlines()
    rounds = [entry.strip() for entry in lines]

    for round in rounds:
        opponentShape = input[round[0]]
        myGoal = input[round[2]]

        if (opponentShape, myGoal) in [('Rock', 'Draw'), ('Paper', 'Lose'), ('Scissors', 'Win')]:
            totalScorePart2 += (pointsOutcome[myGoal] + pointsShape['Rock'])
        elif (opponentShape, myGoal) in [('Rock', 'Win'), ('Paper', 'Draw'), ('Scissors', 'Lose')]:
            totalScorePart2 += (pointsOutcome[myGoal] + pointsShape['Paper']) 
        else:
            totalScorePart2 += (pointsOutcome[myGoal] + pointsShape['Scissors'])

    print('Your total score is: ')
    print(totalScorePart2)