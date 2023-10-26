def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    elif (
            (p1 == "rock" and p2 == "scissors") or
            (p1 == "scissors" and p2 == "paper") or
            (p1 == "paper" and p2 == "rock")
    ):
        return "Player 1 won!"
    else:
        return "Player 2 won!"
        return p1win

result = rps("scissors", "paper")
print(result)

# best practise
# def rps(p1, p2):
#     beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
#     if beats[p1] == p2:
#         return "Player 1 won!"
#     if beats[p2] == p1:
#         return "Player 2 won!"
#     return "Draw!"
