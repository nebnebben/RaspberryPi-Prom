import threading


def worker():
    """thread worker function"""
    print('Worker')

def printname():
	print('Name')

threads = []
a = threading.Thread(target=printname)
a.start()
threads.append(a)
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
