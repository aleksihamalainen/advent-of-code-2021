values = []

lists = [[] for _ in range(12)]

with open('input.txt') as f:
    for line in f:
        values.append(line)
        for index, val in enumerate(line.strip()):
            lists[index].append(val)

most_frequent = []

for l in lists:
    most_frequent.append(max(set(l), key = l.count))

temp = ""
temp2 = ""

gamma_rate = temp.join(most_frequent)
opposite = []

for i in range(len(gamma_rate)):
    val = '0' if gamma_rate[i] == '1' else '1'
    opposite.append(val)

epsilon_rate = temp2.join(opposite)

print(int(gamma_rate, 2) * int(epsilon_rate, 2))

generator_ratings = values
scrubber_ratings = values

for i in range(12):
    zeros = sum([1 for rating in generator_ratings if rating[i] == '0'])
    ones = len(generator_ratings) - zeros
    if len(generator_ratings) == 1:
        break
    if ones >= zeros:
        generator_ratings = [rating for rating in generator_ratings if rating[i] == '1']
    else:
        generator_ratings = [rating for rating in generator_ratings if rating[i] == '0']

for i in range(12):
    zeros = sum([1 for rating in scrubber_ratings if rating[i] == '0'])
    ones = len(scrubber_ratings) - zeros
    if len(scrubber_ratings) == 1:
        break
    if ones < zeros:
        scrubber_ratings = [rating for rating in scrubber_ratings if rating[i] == '1']
    else:
        scrubber_ratings = [rating for rating in scrubber_ratings if rating[i] == '0']

generator_rating = int(generator_ratings[0], 2)
scrubber_rating = int(scrubber_ratings[0], 2)

print(generator_rating * scrubber_rating)