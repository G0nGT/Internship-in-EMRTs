from collections import deque

CAP_3 = 3
CAP_5 = 5
TARGET = 4


def get_next_states(state):
    bucket_3, bucket_5 = state

    possible_states = []

    possible_states.append((CAP_3, bucket_5))
    possible_states.append((bucket_3, CAP_5))

    possible_states.append((0, bucket_5))
    possible_states.append((bucket_3, 0))

    amount = min(bucket_3, CAP_5 - bucket_5)
    possible_states.append((bucket_3 - amount, bucket_5 + amount))

    amount = min(bucket_5, CAP_3 - bucket_3)
    possible_states.append((bucket_3 + amount, bucket_5 - amount))

    return possible_states


def solve():
    start = (0, 0)

    queue = deque()
    queue.append((start, [start]))

    visited = set()
    visited.add(start)

    while queue:
        current_state, path = queue.popleft()

        bucket_3, bucket_5 = current_state

        if bucket_3 == TARGET or bucket_5 == TARGET:
            return path

        for next_state in get_next_states(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))

    return None


solution = solve()

if solution:
    print("Solution:")
    for state in solution:
        print(state)
else:
    print("No solution found.")