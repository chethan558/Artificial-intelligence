import random
import math

def cost(state):
    conflicts = 0

    for i in range(8):
        for j in range(i + 1, 8):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts



def generate_neighbor(current):
    next_state = current.copy()

    i, j = random.sample(range(8), 2)

    next_state[i], next_state[j] = next_state[j], next_state[i]

    return next_state



def simulated_annealing():

    current = random.sample(range(8), 8)

    T = 100

    while T > 0:

        next_state = generate_neighbor(current)

        delta_E = cost(current) - cost(next_state)

        if delta_E > 0:
            current = next_state

        else:
            P = math.exp(delta_E / T)

            if random.random() < P:
                current = next_state

        print("Temperature:", round(T, 2))
        print("Current State:", current)
        print("Current Cost:", cost(current))
        print("----------------------")

        if cost(current) == 0:
            break

        T = T * 0.95

    return current



solution = simulated_annealing()

print("\nFinal Solution:", solution)
print("Final Cost:", cost(solution))

if cost(solution) == 0:
    print("8-Queens solution found!")
else:
    print("Solution not found.")
