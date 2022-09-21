#Rob Hughes

indNum = int(input("Enter the tile order: "))

def getZero(indNum):
	if len(str(indNum))==8:
		return 0
	for i in range(9):
		x = indNum % 10
		indNum = int(indNum/10)
		if x==0:
			break
	return 8-i

def moveTile(indNum):		
	zeroIndex = getZero(indNum)
	indString = str(indNum)
	movedTiles = []
	if len(indString)==8:
		indString = '0' + indString

	if zeroIndex==0:
		final = switch(indString, zeroIndex, 1)		
		movedTiles.append([int(final),indNum])
		final = switch(indString, zeroIndex, 3)
		movedTiles.append([int(final),indNum])
	elif zeroIndex==1:
		final = switch(indString, zeroIndex, 0)	
		final = final[1:]
		movedTiles.append([int(final),indNum])
		final = switch(indString, zeroIndex, 2)
		movedTiles.append([int(final),indNum])
		final = switch(indString, zeroIndex, 4)
		movedTiles.append([int(final),indNum])
	elif zeroIndex==2:
		final = switch(indString, zeroIndex, 1)			
		movedTiles.append([int(final),indNum])
		final = switch(indString, zeroIndex, 5)
		movedTiles.append([int(final),indNum])
	elif zeroIndex==3:
		final = switch(indString, zeroIndex, 0)			
		final = final[1:]
		movedTiles.append([int(final),indNum])
		final = switch(indString, zeroIndex, 4)
		movedTiles.append([int(final),indNum])
		final = switch(indString, zeroIndex, 6)
		movedTiles.append([int(final),indNum])
	elif zeroIndex==4:
		final = switch(indString, zeroIndex, 1)			
		movedTiles.append([int(final),indNum])
		final = switch(indString, zeroIndex, 3)
		movedTiles.append([int(final),indNum])
		final = switch(indString, zeroIndex, 5)
		movedTiles.append([int(final),indNum])
		final = switch(indString, zeroIndex, 7)
		movedTiles.append([int(final),indNum])
	elif zeroIndex==5:
		final = switch(indString, zeroIndex, 2)			
		movedTiles.append([int(final),indNum])
		final = switch(indString, zeroIndex, 4)
		movedTiles.append([int(final),indNum])
		final = switch(indString, zeroIndex, 8)
		movedTiles.append([int(final),indNum])
	elif zeroIndex==6:
		final = switch(indString, zeroIndex, 3)			
		movedTiles.append([int(final),indNum])
		final = switch(indString, zeroIndex, 7)
		movedTiles.append([int(final),indNum])
	elif zeroIndex==7:
		final = switch(indString, zeroIndex, 4)				
		movedTiles.append([int(final),indNum])
		final = switch(indString, zeroIndex, 6)
		movedTiles.append([int(final),indNum])
		final = switch(indString, zeroIndex, 8)
		movedTiles.append([int(final),indNum])
	elif zeroIndex==8:
		final = switch(indString, zeroIndex, 5)			
		movedTiles.append([int(final),indNum])
		final = switch(indString, zeroIndex, 7)
		movedTiles.append([int(final),indNum])
	return movedTiles

def switch(strr, a, b):	
	t = list(strr)
	temp = t[a]
	t[a] = t[b]
	t[b] = temp
	return ''.join(t)

Q = []								
Q.append([indNum,111111111])		
moves = 0							
nodes = 0							
last = indNum
while Q:
	x = Q.pop(0)					
	nodes+=1
	if x[0]==last:
		moves+=1
	listing = moveTile(x[0])		
	for i in listing:				
		if i[0]==x[1]:
			listing.remove(i)
			break
	if listing[len(listing)-1][1]==last:			
		last = 	listing[len(listing)-1][0]	
	for i in listing:
		if (i[0] == 123456780):						
			print("Number of moves - " + str(moves+1))
			exit(0)
		Q.append(i)