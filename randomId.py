import random
try:
    with open('randomid.txt', 'r') as storage:
        print("Loaded " + str(len(storage.readlines())) + " Id's")
except:
    with open('randomid.txt', 'a') as newfile:
        print("[ID-GEN] No storage found, creating one")
def randomId(length, spacing, lc = True, uc= True, num= True):
    lowerCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upperCase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    categories = []
    if lc: categories.extend(lowerCase)
    if uc: categories.extend(upperCase)
    if num: categories.extend(numbers)
    idLen = range(0,length)
    randId = ""
    for c in idLen:
        if c % spacing == 0: randId = randId + '-'
        randId = randId + random.choice(categories)
    with open('randomid.txt', 'r+') as data:
        if randId + "\n" in data.readlines():
            print("[ID-GEN] Found double")
        else:
            data.write(randId[1:] + "\n")
    return randId[1:]

if __name__ == "__main__":
    randomId(20, 4, True, True, True)

