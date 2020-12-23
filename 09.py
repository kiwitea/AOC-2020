from typing import List
import runner
from pathlib import Path


def pairwise_sums(preamble: List[int]):
    sums = []
    for i, x in enumerate(preamble):
        for j, y in enumerate(preamble[i+1:]):
            sums.append(x + y)
    return sums

def is_valid(preamble: List[int], value: int) -> bool:
    # preamble is list of N number
    if len(preamble) != 25:
        raise ValueError('Preamble must have 25 entries.')
    sum_matrix = pairwise_sums(preamble)
    if len(sum_matrix) != ((25*25 - 25) / 2):
        raise ValueError(f'sum matrix should have 300 entries but has {len(sum_matrix)}')
    return value in sum_matrix
    

def part1(data):
    all_numbers = list(map(int, data.splitlines()))
    N = 25
    
    for i in range(len(all_numbers)):
        if not is_valid(all_numbers[i:i+N], all_numbers[i+25]):
            return all_numbers[i+25]


def part2(data):
    invalid_number = part1(data)
    all_numbers = list(map(int, data.splitlines()))
    
    for start in range(len(all_numbers)):
        for end in range(start + 2, len(all_numbers)):
            sequence = all_numbers[start:end]
            x = sum(sequence)
            if x == invalid_number:
                print(f'{start} --> {end}')
                print(sequence)
                return min(sequence) + max(sequence)
            elif x > invalid_number:
                break

runner.run(day=int(Path(__file__).stem))