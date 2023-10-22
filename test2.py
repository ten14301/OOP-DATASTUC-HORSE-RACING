import random
from horse import Horse_brown, Horse_black, Horse_white, Horse_grey, Horse_red

def monte_carlo_horse_racing(num_iterations):
    wins = [0, 0, 0, 0, 0]
    losses = [0, 0, 0, 0, 0]
    horses = [Horse_brown(0, 0), Horse_black(0, 0), Horse_white(0, 0), Horse_grey(0, 0), Horse_red(0, 0)]

    for _ in range(num_iterations):
        # จำลองการแข่งขัน
        winning_horse_idx = random.randint(0, 4)
        player_choice_idx = random.randint(0, 4)
        winning_horse = horses[winning_horse_idx]
        player_choice = horses[player_choice_idx]

        if player_choice_idx == winning_horse_idx:
            wins[player_choice_idx] += 1
        else:
            losses[player_choice_idx] += 1

    win_rates = [wins[i] / num_iterations for i in range(5)]
    loss_rates = [losses[i] / num_iterations for i in range(5)]

    return win_rates, loss_rates

num_iterations = 10000
win_rates, loss_rates = monte_carlo_horse_racing(num_iterations)

for i, horse in enumerate(["Horse Brown", "Horse Black", "Horse White", "Horse Grey", "Horse Red"]):
    win_rate_percentage = win_rates[i] * 100
    loss_rate_percentage = loss_rates[i] * 100
    print(f"{horse} - Win Rate: {win_rate_percentage:.2f}%, Loss Rate: {loss_rate_percentage:.2f}%")
