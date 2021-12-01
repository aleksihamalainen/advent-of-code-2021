input = []

with open('input.txt') as f:
    for line in f:
        input.append(int(line))

count = 0

for i in range(len(input) - 1):
    if input[i + 1] > input[i]:
        count += 1

print(count)

window_count = 0

sliding_windows = [input[i:i+3] for i in range(0, len(input), 1)]

for i in range(len(sliding_windows) - 1):
    if sum(sliding_windows[i + 1]) > sum(sliding_windows[i]):
        window_count += 1

print(window_count)