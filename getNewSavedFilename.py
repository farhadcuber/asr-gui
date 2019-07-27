from os import listdir
from os.path import isfile, join
import re

def getFilename(dir):
    
    dirFiles = [f for f in listdir(dir) if isfile(join(dir, f))]

    usedNums = list()

    for f in dirFiles:
        matchResult = re.match('rec\d+\.wav', f)
        
        if matchResult is not None:
            usedNums.append(int(f[3:-4]))
    
    num = getMinUnusedNaturalNum(usedNums)

    return join(dir, 'rec%s.wav' % str(num).zfill(4))


def getMinUnusedNaturalNum(nums):

    nums.sort()

    counter = 0
    for num in nums:
        if num != counter:
            break
        counter += 1
    
    return counter
    