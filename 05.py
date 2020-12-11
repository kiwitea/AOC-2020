# rows: 0 - 127
# cols: 0 - 7

# row bits (7): F=0, B=1
# col bits (3): L=0, R=1

import numpy as np


def get_row_col(binary: str) -> (int, int):
  row = int(binary[:7], 2)
  col = int(binary[7:], 2)
  return row, col


def get_id(binary: str) -> int:
  row = int(binary[:7], 2)
  col = int(binary[7:], 2)
  return row * 8 + col


def convert_to_binary(data):
  # convert to binary
  replacements = [('F', '0'), ('B', '1'), ('L', '0'), ('R', '1')]
  for repl in replacements:
    data = data.replace(*repl)
  return data


def part1(data):
  binary = convert_to_binary(data)
  ids = sorted(map(get_id, binary.splitlines()))
  return ids[-1]

def part2(data):
  binary = convert_to_binary(data)
  people = list(map(get_row_col, binary.splitlines()))
  people = sorted(people)

  first_row = people[0][0]
  last_row = people[-1][0]
  n_rows = last_row - first_row + 1

  print(first_row, last_row, n_rows)

  seats = np.zeros((last_row + 1, 8), dtype=np.bool)
  print(seats.shape)

  seats[tuple(zip(*people))] = True

  print(seats.sum(), len(people))
  assert seats.sum() == len(people)

  print(people[0], people[-1])
  print(seats[:first_row+1, :])
  
  free_seats = np.where(seats[first_row:last_row, :] == 0)

  my_row, my_col = free_seats[0][-1] + first_row, free_seats[1][-1]
  print(my_row, my_col)
  print(seats[my_row, my_col])

  print(seats[my_row-2:my_row+2, :])

  return my_row * 8 + my_col