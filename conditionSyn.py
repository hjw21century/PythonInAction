from threading import Thread, Condition
import time

items = []
condition = Condition()

class consumer(Thread):
	def __init__(self):
		Thread.__init__(self)

	def consume(self):
		global condition
		global items

		condition.acquire()
		if len(items) == 0:
			print("Consumer notify : no item to consume")
			print(time.localtime())
			condition.wait()#block here until notify is called by another thread
			print(time.localtime())			
		items.pop()
		print("Consumer notify : consumed 1 item")
		print("Consumer notify : items to consume are "\
			+ str(len(items)))
		condition.notify()
		condition.release()

	def run(self):
		for i in range(0,20):
			time.sleep(3)
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
		for i in range(0,20):
			time.sleep(5)
			self.produce()

if __name__ == '__main__':
	producer = producer()
	consumer = consumer()
	producer.start()
	consumer.start()
	producer.join()
	consumer.join()
