import warnings
from memory_profiler import profile, memory_usage
from line_profiler import LineProfiler
import queue
import threading
import time
import yappi

start = time.time()
exitFlag = 0

yappi.set_clock_type("WALL") #can be CPU clock as well

warnings.filterwarnings("ignore")
check_text1 = "That wh0re gave m3 a very good H4nd j0b hehe"
check_text2 = "I am checking whether the translation has any offensive words. The video is absolutely trash and shit. I hate it, it is fucking annoying. fuck you. GO TO hElL, you dirty scum"
check_text3 = "Profanity, often found in today's online social media, has been used to detect online hate speech. The aims of this study were to investigate the profanity usage on Twitter by different groups of users, and to quantify the effectiveness of using profanity in detecting hate speech. Tweets from three English-speaking countries, Australia, Malaysia, and the United States, were collected for data analysis. Statistical hypothesis tests were performed to justify the difference of profanity usage among the three countries, and a probability estimation procedure was formulated based on Bayes theorem to quantify the effectiveness of profanity-based methods in hate speech detection. Three deep learning methods, long short-term memory (LSTM), bidirectional LSTM (BLSTM), and bidirectional encoder representations from transformers (BERT) are further used to evaluate the effect of profanity screening on building classification model. Our experimental results show that the effectiveness of using profanity in detecting hate speech is questionable. Nevertheless, the results also show that for Australia tweets, where profanity is more associated with hatred, profanity-based methods in hate speech detection could be effective and profanity screening can address the class imbalance issue in hate speech detection. This is evidenced by the performances of using deep learning methods on the profanity screened data of Australia data, which achieved a classification f1-score greater than 0.84."


test_string= "small"
module_name = "better_profanity"
requests = 5
class libraries(object):
    
    # @yappi.profile(clock_type= "wall", profile_builtins=False) #,stream = fp
    def func1(self, string):        
        from better_profanity_detector import detect
        detect(string) 
    
    # @profile(precision=4)
    def func2(self, string):
        from profanity_filter_detector import detect
        detect(string)
        
    # @profile(precision=4)
    def func3(self, string):
        from profanityfilter_detector import detect
        detect(string)
    
    # @profile(precision=4)
    def func4(self, string):
        from profanity_detector import detect
        detect(string)

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
      test_string = "small"
      if (test_string == "small"):
        self.test_string = check_text1
      elif(test_string == "medium"):
        self.test_string = check_text2
      elif (test_string == "large"):
        self.test_string = check_text3   
        
      process_data(self.name, self.q, self.test_string, self.module_name)
      print("Exiting " + self.name)

def process_data(threadName, q, test_string, module_name):
   while not exitFlag:
      queueLock.acquire()
      if not workQueue.empty():
        data = q.get()
        print("%s processing %s on module %s" % (threadName, data, module_name))
        lib = libraries()
        if (module_name == "better_profanity"):
          lib.func1(test_string)
        elif (module_name == "profanity_filter"):
          lib.func2(test_string)
        elif(module_name == "profanityfilter"):
          lib.func3(test_string)
        elif(module_name == "profanity"):
          lib.func4(test_string)
          
        queueLock.release()

        
      else:
        queueLock.release()
      time.sleep(1)

#4 threads
threadList = ["Thread-1", "Thread-2", "Thread-3", "Thread-4"]

#*1024 later

# nameList = [test_string] * 5   
# nameList = [check_text1, check_text2, check_text3] 
# test_string = small_string
# string_size = "Small"
nameList = [test_string] * requests
queueLock = threading.Lock()

#queue size will be 1024
workQueue = queue.Queue(requests)
threads = []
threadID = 1

yappi.start()

# Create new threads
for tName in threadList:
   thread = myThread(threadID, tName, workQueue, test_string, module_name)
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

yappi.stop()
stop = time.time()
print("Time Consumed (Latency): {} secs".format(stop - start))

# retrieve thread stats by their thread id (given by yappi)
threads = yappi.get_thread_stats()
for thread in threads:
    print("")
    print("Function stats for (%s) (%d)" % (thread.name, thread.id))  # it is the Thread.__class__.__name__
    yappi.get_func_stats(ctx_id=thread.id).print_all()
    # print("Memory usage:", yappi.get_mem_usage(thread.id))  

print("Line Profiling Summary:")
yappi.get_thread_stats().print_all()
#ttot = total time taken by the thread
    
    


