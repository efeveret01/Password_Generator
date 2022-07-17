import random


def passwordGen(selections, passSize):
    lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    numbs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    special = ["!","£","$","%","^","&","*","(",")","_","+","=","@","#","~","<",">","/","?",".",",","|",";",":","-"]
    caps = []

    endPass = ""

    selected = selections
    passLenght = passSize

    randOne = []
    seeingPass = set({})
    looper = True
    count = 0

    for x in lower:
        caps.append(x.upper())

    for x in selected:
        if x == 1:
            randOne.append(count)
            looper = False
        count += 1


    while looper == False:
        for x in range(passLenght):
            xs = random.choice(randOne)
            if xs == 0:
                endPass = endPass + random.choice(lower)
                seeingPass.add(0)
            if xs == 1:
                endPass = endPass + random.choice(numbs)
                seeingPass.add(1)
            if xs == 2:
                endPass = endPass + random.choice(special)
                seeingPass.add(2)
            if xs == 3:
                endPass = endPass + random.choice(caps)
                seeingPass.add(3)

        if len(seeingPass) == len(randOne):
            break
        
        endPass = ""
        seeingPass = set({})

    return endPass



    

