from random import randint
def randomlength():
    ran = randint(0, 40)
    for i in range (ran):
        print(i)
    return(ran)

print('i printed out', randomlength(), 'values')