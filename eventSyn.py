import time
from threading import Thread, Event
import random

items = []
event = Event()
class consumer(Thread):
	def __init__(self, items, event):
		Thread.__init__(self)
		self.items = items
		self.event = event

	def run(self):
		while True:
			time.sleep(5)
			self.event.wait()#block here until set is called by another thread 
			item = self.items.pop()
			print("Consumer notify : %d popped from list by %s -----item count %d"\
				%(item, self.name, len(items)))

class producer(Thread):
	def __init__(self, intgers, event):
		Thread.__init__(self)
		self.items = items
		self.event = event

	def run(self):
		global item
		for i in range(100):
			time.sleep(1)
			item = random.randint(0, 256)
			self.items.append(item)
			print("Producer notify : item N %d appended \
				to list by %s"\
				%(item, self.name))
			#print(time.localtime())
			self.event.set()
			#print(time.localtime())
			print("Producer notify : event cleared by %s \n"\
				% self.name)
			#self.event.clear()
			#print(time.localtime())

if __name__ == '__main__':
	t1 = producer(items, event)
	t2 = consumer(items, event)
	t1.start()
	t2.start()
	t1.join()
	t2.join()

		
