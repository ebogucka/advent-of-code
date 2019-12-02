#!/usr/bin/env python
# https://adventofcode.com/2019/day/2


def load():
    with open("input") as f:
        return [int(i) for i in f.read().split(",")]


def replace(program, noun, verb):
    program[1] = noun
    program[2] = verb


def execute(program):
    for i in range(0, len(program), 4):
        opcode = program[i]
        if opcode == 99:
            break
        if opcode == 1:
            program[program[i + 3]] = program[program[i + 1]] + program[program[i + 2]]
        elif opcode == 2:
            program[program[i + 3]] = program[program[i + 1]] * program[program[i + 2]]

    return program[0]


# part 1
program = load()
replace(program, 12, 2)
print(execute(program))

# part 2
for noun in range(99):
    for verb in range(99):
        program = load()
        replace(program, noun, verb)
        if execute(program) == 19_690_720:
            print(f"noun={noun}, verb={verb}")
            break
