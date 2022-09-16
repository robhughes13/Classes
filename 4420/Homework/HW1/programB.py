# Rob Hughes

TILE_COLS= 3
TILE_ROWS= 3

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
