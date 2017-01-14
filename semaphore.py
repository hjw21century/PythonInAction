import threading 
import time
import random

semaphore = threading.Semaphore(0)

def consumer():
	print("consumer is waiting.")
	semaphore.acquire()#block here until release is called
	print("Consumer notify: consumed item number %s" %item)

def producer():
	global item
	time.sleep(10)
	item = random.randint(0,1000)
	print("producer notify: produced item number %s" %item)

	semaphore.release()

if __name__ == '__main__':
	for x in range(1,5):
		t1 = threading.Thread(target=producer)
		t2 = threading.Thread(target=consumer)
		t2.start()
		t1.start()
		
		t1.join()
		t2.join()
	print("program terminated")
