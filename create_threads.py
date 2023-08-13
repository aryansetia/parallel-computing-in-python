import time 
from threading import Thread

# def do_work():
#     print("starting work")
#     time.sleep(1)
#     print('finished work')

# for _ in range(5):
#     do_work() 

def do_work():
    print("starting work")
    i = 0
    for _ in range(200000000):
        i+=1 
    print("finished work")

for _ in range(5):
    t = Thread(target=do_work, args=())
    t.start()
