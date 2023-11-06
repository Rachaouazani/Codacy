import random

# Define the bandit arms with different reward distributions
arms = [
    {'name': 'Arm 1', 'mean': 5, 'std_dev': 1},
    {'name': 'Arm 2', 'mean': 3, 'std_dev': 1},
    {'name': 'Arm 3', 'mean': 4, 'std_dev': 1},
]

# Number of rounds for the simulation
num_rounds = 1000

# Initialize variables to store rewards and arm selections
total_reward_epsilon_greedy = 0
total_reward_ucb = 0

# Epsilon value for epsilon-greedy strategy
epsilon = 0.1

# Lists to store rewards for each strategy
epsilon_greedy_rewards = []
ucb_rewards = []

for round in range(num_rounds):
    # Implement epsilon-greedy strategy
    if random.random() < epsilon:
        # Explore: choose a random arm
        chosen_arm = random.choice(arms)
    else:
        # Exploit: choose the arm with the highest estimated value
        chosen_arm = max(arms, key=lambda arm: arm['mean'])

    # Collect reward from the chosen arm
    reward = random.gauss(chosen_arm['mean'], chosen_arm['std_dev'])

    # Update rewards and arm selections
    if chosen_arm == arms[0]:
        epsilon_greedy_rewards.append(reward)
    elif chosen_arm == arms[1]:
        epsilon_greedy_rewards.append(reward)
    elif chosen_arm == arms[2]:
        epsilon_greedy_rewards.append(reward)

# Print the total reward for epsilon-greedy
total_reward_epsilon_greedy = sum(epsilon_greedy_rewards)
print(f'Total reward for epsilon-greedy: {total_reward_epsilon_greedy}')
