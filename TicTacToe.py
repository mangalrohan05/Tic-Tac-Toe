myList = [' ']*10
s = '|'
choice = 'O'
pos = (-1)


# 
def check():
    if ' ' not in myList:
        print('It\'s a tie')
        return True
    return False

# 
def user():
    global choice 
    if choice == 'X':
        choice = 'O'
    else:
        choice = 'X'
    position()

# 
def display():
    print(myList[0], s, myList[1], s, myList[2])
    print(myList[3], s, myList[4], s, myList[5])
    print(myList[6], s, myList[7], s, myList[8])

# 
def position():
    pos = -1
    while not pos in range(0, 9):
        pos = int(input('Enter a position for {}: '.format(choice)))
    update(pos)

# 
def update(pos):
    checkPos(pos)
    myList[pos] = choice
    display()
# 
def checkPos(pos):
    if not myList[pos] == ' ':
        print('position already occupied by {}'.format(myList[pos]))
        position(-1)
    else:
        return
#  
def winCheck():
    global myList
    global choice

    return (myList[0] == myList[1] == myList[2] == choice or 
        myList[3] == myList[4] == myList[5] == choice or 
        myList[6] == myList[7] == myList[8] == choice or 
        myList[0] == myList[3] == myList[6] == choice or
        myList[1] == myList[4] == myList[7] == choice or
        myList[2] == myList[5] == myList[8] == choice or
        myList[0] == myList[4] == myList[8] == choice or 
        myList[2] == myList[4] == myList[6] == choice)


            
def playGame():
    return(input('Do you want to play game (yes, no): ').upper())
            
def startGame():

    while True:

        if(winCheck()):
            print('Congrats {}!, you have won the game!'.format(choice))
            break

        if(check()):
            break
        
        user()

start = playGame()

if(start == 'YES'):
    display()
    startGame()
