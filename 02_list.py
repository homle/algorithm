#python列表类型不同操作的时间效率

from timeit import Timer

def t1():
    l1 = []
    for i in range(1000):
        l1 = l1+[i]

def t2():
    l2 = []
    for i in range(1000):
        l2.append(i)

def t3():
    l3 = [i for i in range(1000)]

def t4():
    l4 = list(range(1000))

def t5():
    l5 = []
    for i in range(1000):
        l5.extend([i])

def t6():
    l6 = []
    for i in range(1000):
        l6.insert(0,i)

t11 = Timer("t1()","from __main__ import t1")
print("+",t11.timeit(number=1000),"seconds")

t22 = Timer("t2()","from __main__ import t2")
print("append",t22.timeit(number=1000),"seconds")

t33 = Timer("t3()","from __main__ import t3")
print("列表生成器[]",t33.timeit(number=1000),"seconds")

t44 = Timer("t4()","from __main__ import t4")
print("list(range)",t44.timeit(number=1000),"seconds")

t55 = Timer("t5()","from __main__ import t5")
print("extend",t55.timeit(number=1000),"seconds")

t66 = Timer("t6()","from __main__ import t6")
print("insert",t66.timeit(number=1000),"seconds")




