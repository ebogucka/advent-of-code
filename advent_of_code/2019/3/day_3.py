#!/usr/bin/env python
# https://adventofcode.com/2019/day/3

cables = []
with open("input") as f:
    i = 0
    for line in f.readlines():
        cables.append([])
        x = 0
        y = 0
        for segment in line.split(","):
            length = int(segment[1:])
            if segment.startswith("U"):
                for j in range(length):
                    y = y + 1
                    cables[i].append((x, y))
            elif segment.startswith("D"):
                for j in range(length):
                    y = y - 1
                    cables[i].append((x, y))
            elif segment.startswith("R"):
                for j in range(length):
                    x = x + 1
                    cables[i].append((x, y))
            elif segment.startswith("L"):
                for j in range(length):
                    x = x - 1
                    cables[i].append((x, y))
        i = i + 1

min_distance = float("inf")
for point in set(cables[0]).intersection(cables[1]):
    distance = abs(point[0]) + abs(point[1])
    if distance < min_distance:
        min_distance = distance
print(f"Min distance: {min_distance}")
