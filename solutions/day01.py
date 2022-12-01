#!/usr/bin/env python

import fileinput
import heapq


def parse_input():
    elves = []
    elf = []
    for line in fileinput.input():
        line = line.rstrip()
        if line == "":
            elves.append(elf)
            elf = []
            continue
        elf.append(int(line))
    return elves


def main():
    elves = parse_input()
    most_cals = max(elves, key=lambda n: sum(n))
    print(sum(most_cals))

    top_3_cals = heapq.nlargest(3, elves, key=lambda n: sum(n))
    print(sum(map(lambda n: sum(n), top_3_cals)))


if __name__ == "__main__":
    main()
