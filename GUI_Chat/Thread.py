import threading

def m1():
    for i in range(5):
        print("One")

def m2():
    for i in range(5):
        print("Two")

def m3():
    for i in range(5):
        print("Three")                

# m1()
# m2()
# m3()

t_m1 = threading.Thread(target=m1)
t_m2 = threading.Thread(target=m2)
t_m3 = threading.Thread(target=m3)

t_m3.start()
t_m1.start()
t_m2.start()
