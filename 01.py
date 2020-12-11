import numpy as np
from io import StringIO


def part1(data):
    # Data is automatically read from 01.txt
    T = 2020

    a = np.genfromtxt(StringIO(data)).astype(int)
    a = a[a <= T]

    sums = a.reshape(1, -1) + a.reshape(-1, 1)
    indices = np.where(sums == T)

    A = a[indices[0][0]]
    B = a[indices[1][0]]

    print(A, B, A+B)
    return A * B


def part2(data):
  T = 2020

  a = np.genfromtxt(StringIO(data)).astype(int)
  a = a[a <= T]

  sums = a.reshape(1, 1, -1) + a.reshape(1, -1, 1) + a.reshape(-1, 1, 1)
  indices = np.where(sums == T)

  A = a[indices[0][0]]
  B = a[indices[1][0]]
  C = a[indices[2][0]]

  print(A, B, C, A+B+C)
  return A * B * C