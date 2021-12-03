dict = {
    'forward': 0,
    'up': 0,
    'down': 0
}

commands = []

with open('input.txt') as f:
    for line in f:
        (key, val) = line.split()
        commands.append([key, int(val)])
        dict[key] += int(val)

print(dict['forward'] * (dict['down'] - dict['up']))

aim = 0
horizontal = 0
depth = 0

for command in commands:
    if command[0] == 'down':
        aim += command[1]
    elif command[0] == 'up':
        aim -= command[1]
    else:
        horizontal += command[1]
        depth += aim * command[1]

print(horizontal * depth)