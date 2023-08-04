tallies = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    # specify more numerals if you wish
}


def roman_num_decimal(roman_num):
    sum = 0
    for i in range(len(roman_num) - 1):
        left = roman_num[i]
        right = roman_num[i + 1]
        if tallies[left] < tallies[right]:
            sum -= tallies[left]
        else:
            sum += tallies[left]
    sum += tallies[roman_num[-1]]
    return sum


print(roman_num_decimal('LXI'))
print(roman_num_decimal('M'))
