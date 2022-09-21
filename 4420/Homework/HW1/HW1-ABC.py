# Rob Hughes
# HW1

import random

MAX_STATES=362880
TILE_COLS= 3
TILE_ROWS= 3

# Program A
def stateLister():
    states= []
    while (len(states)< MAX_STATES):
        count=0
        temp=random.sample(range(9),9)
        for i in range(len(states)):
            if (temp==states[i]):
                count+=1
        if(count==0):
            states.append(temp)
    for i in range(10):
        print(states[i])

# Program B
def getActionState():
    state=[[0,1,2],[3,4,5],[6,7,8]]
    stateNums= input("Current State: ")
    actionNum= int(input("Action(Up-1,Down-2,Left-3,Right-4: "))
    numCount=0
    zeroX=0
    zeroY=0

    for i in range(TILE_ROWS):
        for j in range(TILE_COLS):
            state[i][j]= int(stateNums[numCount])
            numCount+=1
            if (state[i][j]==0):
                zeroX=i
                zeroY=j    
    if (actionNum==1):
        if (zeroX==0):
            print ("invalid action")
        else:
            temp= state[zeroX-1][zeroY]
            state[zeroX-1][zeroY]= 0
            state[zeroX][zeroY]= temp 
    elif (actionNum==2):
        if (zeroX==2):
            print ("invalid action")
        else:
            temp= state[zeroX+1][zeroY]
            state[zeroX+1][zeroY]= 0
            state[zeroX][zeroY]= temp  
    elif (actionNum==3):
        if (zeroY==0):
            print ("invalid action")
        else:
            temp= state[zeroX][zeroY-1]
            state[zeroX][zeroY-1]= 0
            state[zeroX][zeroY]= temp
    elif (actionNum==4):
        if (zeroY==2):
            print ("invalid action")
        else:
            temp= state[zeroX][zeroY+1]
            state[zeroX][zeroY+1]= 0
            state[zeroX][zeroY]= temp
    else:
        print ("Invalid number")

    for i in range(TILE_ROWS):
        for j in range(TILE_COLS):
            print(str(state[i][j]), end="")
    
    return state

# Program C
def threeDivisible():
    state=[[0,1,2],[3,4,5],[6,7,8]]
    stateNums= input("Current State: ") 
    numCount=0
    zeroX=0
    zeroY=0
    for i in range(TILE_ROWS):
        for j in range(TILE_COLS):
            state[i][j]= int(stateNums[numCount])
            numCount+=1
            if (state[i][j]==0):
                zeroX=i
                zeroY=j
                
    row0= str(state[0][0])+ str(state[0][1])+str(state[0][2])
    row1= str(state[1][0])+ str(state[1][1])+str(state[1][2])
    row2= str(state[2][0])+ str(state[2][1])+str(state[2][2])
    print("Current State: " +row0+row1+row2)

    while ((int(row0)%3!=0) or (int(row1)%3!=0) or (int(row2)%3!=0)):
            actionNum=0
            errorFlag=1
            while (errorFlag==1):
                actionNum= random.randint(1,4)
                if (actionNum==1):
                    if (zeroX!=0):
                        temp= state[zeroX-1][zeroY]
                        state[zeroX-1][zeroY]= 0
                        state[zeroX][zeroY]= temp 
                        errorFlag=0
                        zeroX-=1
                elif (actionNum==2):
                    if (zeroX!=2):
                        temp= state[zeroX+1][zeroY]
                        state[zeroX+1][zeroY]= 0
                        state[zeroX][zeroY]= temp
                        errorFlag=0
                        zeroX+=1
                elif (actionNum==3):
                    if (zeroY!=0):
                        temp= state[zeroX][zeroY-1]
                        state[zeroX][zeroY-1]= 0
                        state[zeroX][zeroY]= temp
                        errorFlag=0
                        zeroY-=1
                else:
                    if (zeroY!=2):
                        temp= state[zeroX][zeroY+1]
                        state[zeroX][zeroY+1]= 0
                        state[zeroX][zeroY]= temp
                        errorFlag=0
                        zeroY+=1
                        
            print("Action: " + str(actionNum))
            row0= str(state[0][0])+ str(state[0][1])+str(state[0][2])
            row1= str(state[1][0])+ str(state[1][1])+str(state[1][2])
            row2= str(state[2][0])+ str(state[2][1])+str(state[2][2])
            print("New State: " +row0+row1+row2)

    print("Your Rows Are Divisible By 3!")
                    

                