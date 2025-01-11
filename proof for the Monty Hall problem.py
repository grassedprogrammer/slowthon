import random as r

a = 0
win_no_repick = 0
win_repick = 0
while a < 1000000:
    a+=1
    num_chosen = r.randint(1, 3)
    num_removed = r.randint(1, 3) 
    cor_num = r.randint(1, 3)
    while True:
        if num_removed == num_chosen:
            num_removed = r.randint(1, 3) 
        elif num_removed == cor_num:
            num_removed = r.randint(1, 3)
        else:
            break
    if num_chosen == cor_num:
        win_no_repick+=1
    else:
        win_repick+=1
print("repick" + str(win_repick) + '   NO REPICK:'+ str(win_no_repick))