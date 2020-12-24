from typing import List
import runner
from pathlib import Path
import numpy as np
from collections import Counter

from anytree import Node


def part1(data):
    ratings = list(map(int, data.splitlines()))
    ratings = [0] + sorted(ratings)
    ratings.append(ratings[-1] + 3)
    diffs = np.diff(np.array(ratings))
    cnt = Counter(diffs)
    print(cnt)
    return cnt[1] * cnt[3]  


def valid_sequence(seq):
    diffs = np.diff(seq)
    cnt = Counter(diffs)
    too_large = [diff for diff in cnt.keys() if diff > 3]
    return len(too_large)  == 0


def attach(node: Node, ratings: List[int]):
    children = []
    for i, rating in enumerate(ratings):
        diff = rating - node.name
        if diff <= 3:
            child = Node(rating)
            children.append(child)
            attach(child, ratings[i:])
        else:
            break
    node.children = children


def part2(data):
    ratings = list(map(int, data.splitlines()))
    ratings = sorted(ratings)
    final = ratings[-1] + 3
    
    root = Node(0)
    attach(root, ratings)
    
    valid_leaves = [leaf for leaf in root.leaves if (final - leaf) <= 3]
    print(valid_leaves)
    return len(valid_leaves)
    

runner.run(day=int(Path(__file__).stem))