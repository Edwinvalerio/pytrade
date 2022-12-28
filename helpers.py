def supportAndResistance(stockArray, force=14):
    hashMap = {}
    for price in stockArray:
        if price not in hashMap:
            hashMap[price] = 1
        else:
            hashMap[price] += 1

    piceList = list(hashMap.keys())

    for supportOrResistance in piceList:
        if hashMap[supportOrResistance] < force:
            del hashMap[supportOrResistance]
    return list(hashMap.keys())


print(supportAndResistance([1,1,1,2,2,3,3,3,3,3,3,3],3))