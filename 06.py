from functools import reduce
import runner


def part1(data):

  groups = data.replace('\n\n', ',').replace('\n', '')
  print(groups[:30])
  yes_answers = list(map(set, groups.split(',')))
  print(yes_answers[:5])
  return sum(map(len, yes_answers))


def part2(data):

  groups = data.replace('\n\n', ',')

  yes_answers = []
  for group in groups.split(','):
    yes_answers.append(reduce(lambda x, y: set(x).intersection(set(y)), group.splitlines()))
  return sum(map(len, yes_answers))


runner.run(day=6)