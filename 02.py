import re

def process_line(line: str) -> bool:
  minX, maxX = line.split(' ', 1)[0].split('-')
  c = line.split(':', 1)[0][-1]
  pwd = line.rsplit(' ', 1)[-1]
  return check_pwd(pwd, int(minX), int(maxX), c)

def check_pwd(pwd, minX, maxX, c) -> bool:
  m = re.findall(rf'{c}', pwd)
  return minX <= len(m) <= maxX

def part1(data):
  valid = list(filter(process_line, data.splitlines()))
  return len(valid)


def process_line_2(line: str) -> bool:
  minX, maxX = line.split(' ', 1)[0].split('-')
  c = line.split(':', 1)[0][-1]
  pwd = line.rsplit(' ', 1)[-1]
  return check_pwd_2(pwd, int(minX), int(maxX), c)

def check_pwd_2(pwd, p1, p2, c) -> bool:
  return ((pwd[p1 - 1] == c) + (pwd[p2 - 1] == c)) == 1

def part2(data):
  valid = list(filter(process_line_2, data.splitlines()))
  return len(valid)