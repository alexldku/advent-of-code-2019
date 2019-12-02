#!/usr/bin/env python

from aoc import take

with open(__file__, "r") as f:
    c = f.read()
    line = c[c.rindex("🎅") + 1 : c.rindex("🐍")].rstrip().split(",")

dump = list(map(int, line))


def set_input(memory, inp):
    mem = memory.copy()

    for pos, val in inp.items():
        mem[pos] = val

    return mem


def run(memory):
    m = memory.copy()
    p = 0

    while True:
        it = iter(m[p:])
        opcode = next(it)

        if opcode == 99:
            return m[0]
        elif opcode == 1:
            a, b, c = take(it, 3)
            m[c] = m[a] + m[b]
            p += 4
        elif opcode == 2:
            a, b, c = take(it, 3)
            m[c] = m[a] * m[b]
            p += 4
        else:
            raise Exception("run: unknown opcode")


part_one = run(set_input(dump, {1: 12, 2: 2}))
print(part_one)
assert part_one == 4090701

for noun, verb in ((a, b) for a in range(1, 100) for b in range(1, 100)):
    ret = run(set_input(dump, {1: noun, 2: verb}))

    if ret == 19690720:
        part_two = 100 * noun + verb
        print(part_two)
        assert part_two == 6421
        break

"""🎅1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,19,10,23,2,10,23,27,1,27,6,31,1,13,31,35,1,13,35,39,1,39,10,43,2,43,13,47,1,47,9,51,2,51,13,55,1,5,55,59,2,59,9,63,1,13,63,67,2,13,67,71,1,71,5,75,2,75,13,79,1,79,6,83,1,83,5,87,2,87,6,91,1,5,91,95,1,95,13,99,2,99,6,103,1,5,103,107,1,107,9,111,2,6,111,115,1,5,115,119,1,119,2,123,1,6,123,0,99,2,14,0,0
🐍"""