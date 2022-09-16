#Rob Hughes

import random
MAX_STATES=362880


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
