from pydantic import BaseModel, Field, constr, validator
from enum import Enum


class EyeColor(str, Enum):
  amb = "amb"
  blu = "blu"
  brn = "brn"
  gry = "gry"
  grn = "grn"
  hzl = "hzl"
  oth = "oth"


class Passport(BaseModel):
  byr: constr(min_length=4, max_length=4) = Field(..., description='Birth Year')

  @validator('byr')
  def valid_byr(cls, v):
    if 1920 <= int(v) <= 2002:
      return v
    raise ValueError(f'{v} is not a valid byr')
        
  iyr: constr(min_length=4, max_length=4) = Field(..., description='Issue Year')

  @validator('iyr')
  def valid_iyr(cls, v):
    if 2010 <= int(v) <= 2020:
      return v
    raise ValueError(f'{v} is not a valid iyr')

  eyr: constr(min_length=4, max_length=4) = Field(..., description='Expiration Year')

  @validator('eyr')
  def valid_eyr(cls, v):
    if 2020 <= int(v) <= 2030:
      return v
    raise ValueError(f'{v} is not a valid eyr')

  hgt: constr(regex=r'^[0-9]+(cm|in)$') = Field(..., description='Height')

  @validator('hgt')
  def valid_hgt(cls, v):
    h, unit = int(v[:-2]), v[-2:]
    if unit == 'in':
      if 59 <= h <= 76:
        return v
    elif unit == 'cm':
      if 150 <= h <= 193:
        return v
    else:
      raise ValueError(f'{v} is not a valid hgt')
    raise ValueError(f'{v} is not a valid hgt')

  hcl: constr(regex=r'^#([0-9a-fA-F]){6}$') = Field(..., description='Hair Color')

  ecl: EyeColor = Field(..., description='Eye Color')
  pid: constr(regex=r"^[0-9]{9}$") = Field(..., description='Passport ID')
  cid: str = Field('NP', description='Country ID')


def parse_passport(passport: str) -> dict:
  return dict([(line.split(':')) for line in passport.splitlines()])

def part2(data):
  passports = data.split('\n\n')
  print(len(passports))
  passport_data = [p.replace(' ', '\n') for p in passports
  ]
  passport_dicts = list(map(parse_passport, passport_data))

  count = 0
  for passport in passport_dicts:
    try:
      Passport.parse_obj(passport)
    except ValueError as e:
      print(e)
      continue
    count += 1

  return count