import re
from scipy import spatial as sp

with open('sentences.txt', 'r') as i_file:
    data = i_file.read().lower()

data = re.split('[^a-z]', data)
data = list(set(data))

data = {data[i]: i-1 for i in range(len(data)) if data[i]}

matrix = [[0 for _ in range(254)] for _ in range(22)]


with open("sentences.txt", 'r') as i_file:
    for i in range(22):
        temp = i_file.readline().lower()
        for word in set(re.split('[^a-z]', temp)):
            if word:
                matrix[i][data[word]] += 1

ans_array = [sp.distance.cosine(matrix[0], matrix[i]) for i in range(1, 22)]
min_1, min_2 = ans_array.index(sorted(ans_array)[0]), ans_array.index(sorted(ans_array)[1])
with open('sentences-1.txt', 'w') as o_file:
    o_file.write(f'{min(min_2, min_1)+1} {max(min_2, min_1)+1}')
