#!/usr/bin/python

import queue
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, q):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.q = q
   def run(self):
      print("Starting " + self.name)
      #call moodule condition here and module
      process_data(self.name, self.q)
      print("Exiting " + self.name)

def process_data(threadName, q):
   while not exitFlag:
      queueLock.acquire()
      if not workQueue.empty():
        data = q.get()
        queueLock.release()
        print("%s processing %s" % (threadName, data))
      else:
        queueLock.release()
      time.sleep(1)

#4 threads
threadList = ["Thread-1", "Thread-2", "Thread-3", "Thread-4"]

#*1024 later
test_string = "small string"
nameList = [test_string] * 5    
queueLock = threading.Lock()

#queue size will be 1024
workQueue = queue.Queue(5)
threads = []
threadID = 1

# Create new threads
for tName in threadList:
   thread = myThread(threadID, tName, workQueue)
   thread.start()
   threads.append(thread)
   threadID += 1

# Fill the queue
queueLock.acquire()
for word in nameList:
   workQueue.put(word)
queueLock.release()

# Wait for queue to empty
while not workQueue.empty():
   pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
   t.join()
print("Exiting Main Thread")