# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
from RPS_game import play, quincy
def player(prev_play, opponent_history=[]):
    import random
    # Function to decide the ideal counter move
    def counter_move(predicted_move):
        ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
        return ideal_response.get(predicted_move, random.choice(['R', 'P', 'S']))
    # Initialize the opponent history if it's the first play
    if prev_play == '':
        prev_play = 'P'
        opponent_history.append(prev_play)
        prev_play = 'S'
    opponent_history.append(prev_play)
    quincy_pattern = ["R", "P", "P", "S", "R"]
    if len(opponent_history) >= 5:
        last_five = opponent_history[-5:]
        if last_five == quincy_pattern:
            return 'P'  # Counter 'R' in the repeating pattern
    last_two = "".join(opponent_history[-2:])
    
    # Create and update play order frequency
    play_order = {
        "RR": 0, "RP": 1, "RS": 0,
        "PR": 0, "PP": 0, "PS": 1,
        "SR": 0, "SP": 0, "SS": 0
    }
    play_order[last_two] += 1
    
    # Determine potential plays and their frequencies
    potential_plays = [opponent_history[-1] + move for move in 'RPS']
    sub_order = {k: play_order.get(k, 0) for k in potential_plays}
    
    # Predict the most likely next move
    prediction = max(sub_order, key=sub_order.get, default='R')[-1:]
    
    return counter_move(prediction)

# print(play(player, quincy, 5, verbose=True))