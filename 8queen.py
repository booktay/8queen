import numpy as np

BASE_NUM = np.arange(1, 17, 1).reshape(4, 4)
table = np.arange(0, 16, 1)
np.random.shuffle(table)
table = table.reshape(4, 4)
BASE_NUM[3, 3] = count = 0
while(np.count_nonzero(table - BASE_NUM) > 0):
    print(table)
    key = input('W,A,S,D : ').lower()
    zero = np.where(table == 0)
    x = y = 0
    if(key == 'w' and zero[0] < 3):
        y = 1
    elif(key == 'a' and zero[1] < 3):
        x = 1
    elif (key == 's' and zero[0] > 0):
        y = -1
    elif (key == 'd' and zero[1] > 0):
        x = -1
    if(x + y != 0):
        table[zero] = table[zero[0] + y, zero[1] + x]
        table[zero[0] + y, zero[1] + x] = 0
    count += 1
print("Winner [Moved : %d]" %count)
print(table)
