def whos_first(p1, p2):
    distans = p1.find('B') - p2.find('B')
    if distans < 0:
        return 'p1'
    elif distans > 0:
        return 'p2'
    else:
        return 'tie'