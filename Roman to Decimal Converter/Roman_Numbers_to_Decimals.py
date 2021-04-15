tallies = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

def romannumeral_to_decimal(romannumeral):
    decimal = 0
    for i in range(len(romannumeral) - 1):
        left = romannumeral[i]
        right = romannumeral[i + 1]
        if tallies[left] < tallies[right]:
            decimal -= tallies[left]
        else:
            decimal += tallies[left]
    decimal += tallies[romannumeral[-1]]
    return decimal

print(romannumeral_to_decimal("MMDCCLIV"))