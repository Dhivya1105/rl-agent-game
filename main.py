import random

# Grid size
grid_size = 4

# Positions
agent = [0, 0]
goal = [3, 3]
penalty = [1, 2]

actions = ['up', 'down', 'left', 'right']

def move(agent, action):
    if action == 'up' and agent[0] > 0:
        agent[0] -= 1
    elif action == 'down' and agent[0] < grid_size - 1:
        agent[0] += 1
    elif action == 'left' and agent[1] > 0:
        agent[1] -= 1
    elif action == 'right' and agent[1] < grid_size - 1:
        agent[1] += 1
    return agent

def get_reward(pos):
    if pos == goal:
        return 10
    elif pos == penalty:
        return -10
    else:
        return -1

# Game loop
for step in range(10):
    action = random.choice(actions)
    agent = move(agent, action)
    reward = get_reward(agent)

    print("Step:", step, "Position:", agent, "Action:", action, "Reward:", reward)

    if agent == goal:
        print("🎉 Reached Goal!")
        break
    if agent == penalty:
        print("❌ Hit Penalty!")
        break
