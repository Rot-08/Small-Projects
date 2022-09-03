import random

def dice():
    seed = input("Press any key to roll dice \n")[0]
    output1 = ( ord(seed) * random.randint(0, 10)) % 6
    output2 = ( ord(seed) * random.randint(0, 10)) % 6

    if(output1 == output2 == 6):
        print("Wow!!! You rolled Two Six's... Take another throw")
        dice()
    else:
        print("You rolled: {output1} and {output2} \n ".format(output1 = output1 +1, output2 = output2 +1))


dice()