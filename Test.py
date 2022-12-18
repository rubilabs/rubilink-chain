from ProofOfStake import ProofOfStake
from Lot import Lot
import string
import random

def getRandomString(length):
    letters = string.ascii_lowercase
    resultString = ''.join(random.choice(letters) for i in range(length))
    return resultString

if __name__ == '__main__':
    pos = ProofOfStake()
    pos.update('sakura', 10)
    pos.update('asuka', 100)

    sakuraWins = 0
    asukaWins = 0

    for i in range(100):
        forger = pos.forger(getRandomString(i))
        if forger == 'sakura': 
            sakuraWins += 1
        elif forger == 'asuka':
            asukaWins += 1
    
    print('sakura won:' + str(sakuraWins) + 'times')
    print('asuka won:' + str(asukaWins) + 'times')