def lines_startswith(file, letter):
    
    matches = []
    
    for line in file:
        if line.startswith(letter):
            matches.append(line.rstrip('\n'))

    return matches
    
