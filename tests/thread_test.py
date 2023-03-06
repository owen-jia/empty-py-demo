import threading
import time
import queue

# python thread demo


def my_print(p="empty"):
    print("p", p)


def thread_test(param='first param'):
    print("param:", param)
    print("thread_test...")


def thread_main():
    thread_1=threading.Thread()
    thread_1.__init__(thread_test("am i?"))
    thread_1_data = threading.local
    print(thread_1_data.__name__)
    thread_1.start()
    print("thread_main...")


def time_test():
    timer = threading.Timer(1, my_print)
    timer.start()
    print("time_test...")


def queue_test():
    q = queue.LifoQueue(10)
    q.put(my_print(1))
    q.put(my_print(2))
    q.put(my_print(3))
    print("q size:", q.qsize())
    f_p = q.get()
    print("queue_test...")


if __name__=='__main__':
    queue_test()
