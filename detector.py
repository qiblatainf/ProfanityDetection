# import joblib
# from profanity_check import predict_prob



# prediction = predict_prob(['go to hell, you scum'])
# print(prediction)

from better_profanity import profanity
from memory_profiler import profile
from line_profiler import LineProfiler

# lprofiler = LineProfiler()

# dirty_text = "That l3sbi4n did a very good H4ndjob."

# dirty_text = "heheh"
dirty_text = "That wh0re gave m3 a very good H4nd j0b"

text = "Profanity, often found in today's online social media, has been used to detect online hate speech. The aims of this study were to investigate the profanity usage on Twitter by different groups of users, and to quantify the effectiveness of using profanity in detecting hate speech. Tweets from three English-speaking countries, Australia, Malaysia, and the United States, were collected for data analysis. Statistical hypothesis tests were performed to justify the difference of profanity usage among the three countries, and a probability estimation procedure was formulated based on Bayes theorem to quantify the effectiveness of profanity-based methods in hate speech detection. Three deep learning methods, long short-term memory (LSTM), bidirectional LSTM (BLSTM), and bidirectional encoder representations from transformers (BERT) are further used to evaluate the effect of profanity screening on building classification model. Our experimental results show that the effectiveness of using profanity in detecting hate speech is questionable. Nevertheless, the results also show that for Australia tweets, where profanity is more associated with hatred, profanity-based methods in hate speech detection could be effective and profanity screening can address the class imbalance issue in hate speech detection. This is evidenced by the performances of using deep learning methods on the profanity screened data of Australia data, which achieved a classification f1-score greater than 0.84."

@profile(precision=4)
def detect(string):
    result = profanity.contains_profanity(string)
    print(result)


string = dirty_text
lp = LineProfiler()
lp_wrapper = lp(detect.__wrapped__)
lp_wrapper(string)
lp.print_stats()


# lp_wrapper = lprofiler(detect.__wrapped__)
# profile = LineProfiler(detect(dirty_text))
# # lp_wrapper()
# # lprofiler.print_stats()
# profile.print_stats()
