from functools import reduce


def count_trees(data, col_offset, row_offset):
  m = data.splitlines()
  columns = len(m[0])
  row, col = 0, 0

  n_trees = 0
  while(True):
    row += row_offset
    col = (col + col_offset) % columns

    try:
      n_trees += m[row][col] == '#'
    except IndexError:
      break
    
  return n_trees

def part1(data):
  return count_trees(data, 3, 1)

def part2(data):
  slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
  return reduce((lambda x, y: x*y), [count_trees(data, c, r) for c, r in slopes])