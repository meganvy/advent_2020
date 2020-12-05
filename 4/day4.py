import os
import collections

def part_one():
    passport = {}
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid_passports = []
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, "input.txt"), "r") as f:
        for line in f:
            if line.strip() != "":
                line_info = line.strip().split()
                for info in line_info:
                    key, value = info.split(":")
                    passport[key] = value
            else:
                # print(passport)
                if all ((x in passport.keys() for x in fields)):
                    valid_passports.append(passport)
                passport = {}

    return valid_passports

def part_two():
    preprocessed_passports = part_one()
    valid_passports = len(preprocessed_passports)
    for passport in preprocessed_passports:
        if 'byr' in passport.keys() and not (1920 <= int(passport['byr']) <= 2002):
            valid_passports -=1
            continue
        if 'iyr' in passport.keys() and not (2010 <= int(passport['iyr']) <= 2020):
            valid_passports -=1
            continue
        if 'eyr' in passport.keys() and not (2020 <= int(passport['eyr']) <= 2030):
            valid_passports -=1
            continue
        if 'hgt' in passport.keys():
            height, unit = passport['hgt'][:-2] or '0', passport['hgt'][-2:]
            if unit == "cm":
                if not (150 <= int(height) <= 193):
                    valid_passports -=1
                    continue
            elif unit == "in":
                if not (59 <= int(height) <= 76):
                    valid_passports -=1
                    continue
            else:
                valid_passports -= 1
                continue
        if 'hcl' in passport.keys():
            if (passport['hcl'][0] != "#"):
                valid_passports -=1
                continue
            try:
                convert_to_int = int(passport['hcl'][1:], 16)
            except Exception as e:
                valid_passports -=1
                continue
        if 'ecl' in passport.keys() and passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            valid_passports -=1
            continue
        if 'pid' in passport.keys() and len(passport['pid']) != 9:
            valid_passports -=1
            continue

    return valid_passports

print(len(part_one()))
print(part_two())
