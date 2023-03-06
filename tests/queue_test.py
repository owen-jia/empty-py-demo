import threading
import queue


q = queue.Queue(10)


def worker():
    while True:
        i = q.get()
        print(i)
        q.task_done()


threading.Thread(worker(),daemon=True).start()

for i in range(20):
    q.put(i)

q.join()
print("done")