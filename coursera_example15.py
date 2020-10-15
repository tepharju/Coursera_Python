def lines_startswith(file, letter):
    matches = []

    for line in file:
        if letter in line:
            matches.append(line.rstrip('\n'))

    return matches
