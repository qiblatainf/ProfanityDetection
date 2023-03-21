import warnings
from memory_profiler import profile
from line_profiler import LineProfiler
import queue
import threading
import time

exitFlag = 0

warnings.filterwarnings("ignore")
check_text1 = "That wh0re gave m3 a very good H4nd j0b hehe"
# check_text2 = "I am checking whether the translation has any offensive words. The video is absolutely trash and shit. I hate it, it is fucking annoying. fuck you. GO TO hElL, you dirty scum"
# check_text3 = "Profanity, often found in today's online social media, has been used to detect online hate speech. The aims of this study were to investigate the profanity usage on Twitter by different groups of users, and to quantify the effectiveness of using profanity in detecting hate speech. Tweets from three English-speaking countries, Australia, Malaysia, and the United States, were collected for data analysis. Statistical hypothesis tests were performed to justify the difference of profanity usage among the three countries, and a probability estimation procedure was formulated based on Bayes theorem to quantify the effectiveness of profanity-based methods in hate speech detection. Three deep learning methods, long short-term memory (LSTM), bidirectional LSTM (BLSTM), and bidirectional encoder representations from transformers (BERT) are further used to evaluate the effect of profanity screening on building classification model. Our experimental results show that the effectiveness of using profanity in detecting hate speech is questionable. Nevertheless, the results also show that for Australia tweets, where profanity is more associated with hatred, profanity-based methods in hate speech detection could be effective and profanity screening can address the class imbalance issue in hate speech detection. This is evidenced by the performances of using deep learning methods on the profanity screened data of Australia data, which achieved a classification f1-score greater than 0.84."
small_string = check_text1
medium_string = "B"
large_string = "C"
# string = check_text1

#user-inputs
# test_string = "small string"
# module_name = "better_profanity"

class libraries(object):
    
    # @profile(precision=4)
    def func1(self, string):        
        from better_profanity_detector import detect
        detect(string)
    

    def func2(self, string):
        from profanity_filter_detector import detect
        detect(string)
        
  
    def func3(self, string):
        from profanityfilter_detector import detect
        detect(string)
    
 
    def func4(self, string):
        from profanity_detector import detect
        detect(string)   
# def func1(test_string):        
#         from better_profanity_detector import detect
#         detect(test_string)
    
class myThread (threading.Thread):
   def __init__(self, threadID, name, q, test_string, module_name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.q = q
      self.test_string = test_string
      self.module_name = module_name
      
   def run(self):
      print("Starting " + self.name)
      #call moodule condition here and module
    #   func1(self.test_string)    
      
      process_data(self.name, self.q, self.test_string, self.module_name)
      print("Exiting " + self.name)

def process_data(threadName, q, test_string, module_name):
   while not exitFlag:
      queueLock.acquire()
      if not workQueue.empty():
        data = q.get()
        print("Processing module: " + module_name)
        # print("q = " , q)
        # func1(test_string)
        # l1 = libraries()
        # l1.func3(test_string)
        queueLock.release()
        print("%s processing %s" % (threadName, data))
      else:
        queueLock.release()
      time.sleep(1)

#4 threads
threadList = ["Thread-1", "Thread-2", "Thread-3", "Thread-4"]

#*1024 later

# nameList = [test_string] * 5   
# nameList = [check_text1, check_text2, check_text3] 
test_string = small_string
nameList = [small_string] * 5
queueLock = threading.Lock()

#queue size will be 1024
workQueue = queue.Queue(5)
threads = []
threadID = 1

module_name = ["better_profanity", "profanity_filter", "profanityfilter", "profanity"]

# Create new threads
for tName in threadList:
   thread = myThread(threadID, tName, workQueue, test_string, module_name[threadID-1])
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