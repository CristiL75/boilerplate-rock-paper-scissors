import random

def player(prev_play, opponent_history=[]):
    if prev_play != "":
        opponent_history.append(prev_play)

    # Store the opponent's previous moves
    if len(opponent_history) == 0:
        return random.choice(["R", "P", "S"])

    # Define counter moves
    def counter_move(move):
        if move == "R":
            return "P"
        elif move == "P":
            return "S"
        elif move == "S":
            return "R"

    # Detect simple patterns like RPSR, SPRP etc.
    def detect_pattern():
        if len(opponent_history) < 5:
            return None
        pattern = "".join(opponent_history[-5:])
        # Check common patterns in the opponent's moves
        if pattern == "RPSRP" or pattern == "PSRPS" or pattern == "SRPSR":
            return counter_move(opponent_history[-1])
        return None

    # Counter the most frequent move of the opponent
    def counter_most_frequent():
        if len(opponent_history) < 5:
            return None
        move_counts = {
            "R": opponent_history.count("R"),
            "P": opponent_history.count("P"),
            "S": opponent_history.count("S")
        }
        most_frequent = max(move_counts, key=move_counts.get)
        return counter_move(most_frequent)

    # Use weighted random strategy based on recent history
    def weighted_random_choice():
        move_weights = {
            "R": 1,
            "P": 1,
            "S": 1
        }
        for move in opponent_history[-5:]:
            move_weights[move] += 1
        return random.choices(["R", "P", "S"], weights=[move_weights["R"], move_weights["P"], move_weights["S"]])[0]

    # Apply strategies in order
    move = detect_pattern()  # Detect if there's a pattern
    if not move:
        move = counter_most_frequent()  # If no pattern, counter the most frequent move
    if not move:
        move = weighted_random_choice()  # If no clear strategy, use weighted random choice
    
    return move
