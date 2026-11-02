def cost(state):
    conflicts = 0

    for i in range(4):
        for j in range(i + 1, 4):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts


def generate_neighbors(current):
    neighbors = []

    for i in range(3):
        for j in range(i + 1, 4):
            next_state = current.copy()

            next_state[i], next_state[j] = next_state[j], next_state[i]

            neighbors.append(next_state)

    return neighbors


def neighbor_with_minimum_cost(neighbors):
    best = neighbors[0]

    for neighbor in neighbors:
        if cost(neighbor) < cost(best):
            best = neighbor

    return best


def hill_climbing():

    current = list(map(int, input("Enter 4 values: ").split()))

    while True:

        current_cost = cost(current)

        print("\nCurrent State:", current)
        print("Current Cost:", current_cost)

        if current_cost == 0:
            return current

        neighbors = generate_neighbors(current)

        print("\nNeighbor States:")

        for neighbor in neighbors:
            print(neighbor, "Cost:", cost(neighbor))

        neighbor = neighbor_with_minimum_cost(neighbors)

        print("\nSelected Neighbor:", neighbor)
        print("Neighbor Cost:", cost(neighbor))

        if cost(neighbor) >= current_cost:
            return current

        current = neighbor


solution = hill_climbing()

print("\nFinal Solution:", solution)
print("Final Cost:", cost(solution))
