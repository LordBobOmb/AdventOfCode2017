def manhattanDistanceToMiddle(input):
    currRingWidth = 1;
    maxValue = 1;
    while(maxValue < input):
        currRingWidth += 2
        maxValue = currRingWidth**2

    x = (currRingWidth - 1) / 2
    y = -x
    diff = maxValue - input;
    if diff < currRingWidth:
        x -= diff
        return distance(x,y)
    else:
        x -= currRingWidth - 1
        diff -= currRingWidth - 1
        if(diff < currRingWidth):
            y+= diff
            return distance(x,y)
        else:
            y += currRingWidth - 1
            diff -= currRingWidth - 1
            if(diff < currRingWidth):
                x += diff
                return distance(x,y)
            else:
                x+= currRingWidth - 1
                y-= diff
                return distance(x,y)


def distance(x, y):
    return abs(x) + abs(y)


INPUT = 347991
print(manhattanDistanceToMiddle(INPUT))




