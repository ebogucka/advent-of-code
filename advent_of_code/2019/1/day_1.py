#!/usr/bin/env python
# https://adventofcode.com/2019/day/1


def calculate_fuel_needed(mass):
    return max(0, int(mass) // 3 - 2)


with open("input") as f:
    lines = f.readlines()

# part 1
print(sum([calculate_fuel_needed(mass) for mass in lines]))

# part 2
fuel_total = 0
for module in lines:
    fuel_needed = calculate_fuel_needed(module)
    fuel_total += fuel_needed
    while (calculate_fuel_needed(fuel_needed) > 0):
        fuel_needed = calculate_fuel_needed(fuel_needed)
        fuel_total += fuel_needed
print(fuel_total)
