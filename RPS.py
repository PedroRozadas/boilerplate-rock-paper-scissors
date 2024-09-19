# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    import random

    # Function to decide the ideal counter move
    def counter_move(predicted_move):
        ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
        return ideal_response.get(predicted_move, random.choice(['R', 'P', 'S']))

    # Initialize the opponent history if it's the first play
    if prev_play == '':
        prev_play = 'R'
    
    opponent_history.append(prev_play)

    # Introduce variability to make the strategy less predictable
    if random.random() < 0.3:  # 30% of the time, choose randomly
        return random.choice(['R', 'P', 'S'])

    # Analyze opponent's last two moves to predict the next move
    if len(opponent_history) > 1:
        last_two = "".join(opponent_history[-2:])
        
        # Create and update play order frequency
        play_order = {
            "RR": 0, "RP": 0, "RS": 0,
            "PR": 0, "PP": 0, "PS": 0,
            "SR": 0, "SP": 0, "SS": 0
        }
        play_order[last_two] += 1
        
        # Determine potential plays and their frequencies
        potential_plays = [opponent_history[-1] + move for move in 'RPS']
        sub_order = {k: play_order.get(k, 0) for k in potential_plays}
        
        # Predict the most likely next move
        prediction = max(sub_order, key=sub_order.get, default='R')[-1:]
        return counter_move(prediction)
    
    # Default return if no sufficient history
    return random.choice(['R', 'P', 'S'])