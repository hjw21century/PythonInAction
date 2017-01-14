from threading import Thread, Condition
import time

items = []
condition = Condition()

class consumer(Thread):
	_id = ""
	def __init__(self,id):
		Thread.__init__(self)
		self._id = id

	def consume(self):
		global condition
		global items

		condition.acquire()
		if len(items) == 0:
			print("Consumer %s notify : no item to consume" % self._id)
			#print(time.localtime())
			condition.wait()#block here until notify is called by another thread
			#print(time.localtime())			
		items.pop()
		print("Consumer %s notify : consumed 1 item" % self._id)
		print("Consumer " + self._id + " notify : items to consume are "\
			+ str(len(items)))
		condition.notify()
		condition.release()

	def run(self):
		for i in range(0,20):
			time.sleep(8)
			self.consume()

class producer(Thread):
	def __init__(self):
		Thread.__init__(self)

	def produce(self):
		global condition
		global items

		condition.acquire()
		if len(items) == 10:
			condition.wait()
			print("Producer notify : items produced are "\
				+ str(len(items)))
			print("Producer notify : stop the production!!")
		items.append(1)
		print("Producer notify : total items produced "\
			+ str(len(items)))
		condition.notify()
		condition.release()

	def run(self):
		for i in range(0,40):
			time.sleep(3)
			self.produce()

if __name__ == '__main__':
	producer = producer()
	consumer1 = consumer("111")
	consumer2 = consumer("222")
	producer.start()
	consumer1.start()
	consumer2.start()
	producer.join()
	consumer1.join()
	consumer2.join()
