import time
Xxxtimer_timexxX:float = 0.0

def get_dict_index_value(thing, index, normal):
    if normal == True:
        index+=1
    for key, value in thing.items():
        index-=1
        if index < 1:
            return key, value
    return None

def start_timer():
    global Xxxtimer_timexxX
    Xxxtimer_timexxX = time.time()
def get_timer_time():
    global Xxxtimer_timexxX
    return time.time() - Xxxtimer_timexxX
def stop_timer():
    global Xxxtimer_timexxX
    a = time.time()
    stop_time = a - Xxxtimer_timexxX
    Xxxtimer_timexxX = 0.0
    return stop_time

if __name__ == "__main__":
    start_timer()
    for i in range(1,1000000):print("aye")
    print(get_timer_time())
    print(stop_timer())