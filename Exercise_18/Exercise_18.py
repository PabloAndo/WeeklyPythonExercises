import glob
import time
import threading
from queue import Queue

counts = Queue()


def count_words_file(filename):
    try:
        total = 0
        for one_line in open(filename):
            total += len(one_line.split())
        counts.put(total)
    except Exception:
        pass


def count_words_threading(pattern):
    for one_filename in glob.glob(pattern):
        threading.Thread(target=count_words_file, args=(one_filename,)).start()

    while len(threading.enumerate()) > 1:
        for t in threading.enumerate():
            if threading.currentThread() == t:
                continue
            t.join(0.1)

    total = 0
    while not counts.empty():
        total += counts.get()

    return(total)


def count_words_sequential(pattern):
    total = 0
    for one_filename in glob.glob(pattern):
        try:
            total += len(open(one_filename).read().split())
        except Exception:
            pass

    return total


pattern = 'C:\\Windows\\Temp\\b*'

first = time.time()
print(count_words_sequential(pattern))
second = time.time()
print(count_words_threading(pattern))
third = time.time()

print("Sequential version took {}".format(second - first))
print("Threaded version took {}".format(third - second))
