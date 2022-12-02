file1 = open('input.txt', 'r')
lines = file1.readlines()

# Part 1

# A, X = Rock. B, Y = Paper. C, Z = Scissors.

# Store the possible scores for each move choice (our score when opponent playing against X)
rock_score = [3, 0, 6]
paper_score = [6, 3, 0]
scissors_score = [0, 6, 3]
moves = {'X' : 1, 'Y' : 2, 'Z': 3}
o_moves = {'A' : 0, 'B' : 1, 'C': 2} # Store the array index for the relation score.
move_score = 0
round_score = 0

# Calculate the score for all our moves.

for line in lines:
    move = line.strip().split(" ")
    opponent_move = move[0]
    player_move = move[1]
    move_score += moves[player_move]

    # Calculate the round score (relate player_move with opponent_move)
    if player_move == 'X':
        round_score += rock_score[o_moves[opponent_move]]
    if player_move == 'Y':
        round_score += paper_score[o_moves[opponent_move]]
    if player_move == 'Z':
        round_score += scissors_score[o_moves[opponent_move]]

print(move_score + round_score)

# Part 2
winning_moves = [2, 3, 1]
drawing_moves = [1, 2, 3]
losing_moves = [3, 1, 2]

player_move_score = 0
round_score = 0

for line in lines:
    move = line.strip().split(" ")
    opponent_move = move[0]
    result = move[1]

    # We need to calculate a move for the move_score.
    if result == 'X':
        player_move_score += losing_moves[o_moves[opponent_move]]
    if result == 'Y':
        player_move_score += drawing_moves[o_moves[opponent_move]]
    if result == 'Z':
        player_move_score += winning_moves[o_moves[opponent_move]]

    # Simply add the result that we already know. Use the moves dictionary to convert the move score to a val between 0, 3, 6
    round_score += (moves[result] - 1) * 3

print(round_score + player_move_score)