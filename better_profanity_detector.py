
from better_profanity import profanity



# @profile(precision=4)
def detect(string):
    result = profanity.contains_profanity(string)
    print(result)

# detect(check_text1)
check_text1 = "That wh0re gave m3 a very good H4nd j0b hehe"
check_text2 = "I am checking whether the translation has any offensive words. The video is absolutely trash and shit. I hate it, it is fucking annoying. fuck you. GO TO hElL, you dirty scum"
check_text3 = "Profanity, often found in today's online social media, has been used to detect online hate speech. The aims of this study were to investigate the profanity usage on Twitter by different groups of users, and to quantify the effectiveness of using profanity in detecting hate speech. Tweets from three English-speaking countries, Australia, Malaysia, and the United States, were collected for data analysis. Statistical hypothesis tests were performed to justify the difference of profanity usage among the three countries, and a probability estimation procedure was formulated based on Bayes theorem to quantify the effectiveness of profanity-based methods in hate speech detection. Three deep learning methods, long short-term memory (LSTM), bidirectional LSTM (BLSTM), and bidirectional encoder representations from transformers (BERT) are further used to evaluate the effect of profanity screening on building classification model. Our experimental results show that the effectiveness of using profanity in detecting hate speech is questionable. Nevertheless, the results also show that for Australia tweets, where profanity is more associated with hatred, profanity-based methods in hate speech detection could be effective and profanity screening can address the class imbalance issue in hate speech detection. This is evidenced by the performances of using deep learning methods on the profanity screened data of Australia data, which achieved a classification f1-score greater than 0.84."
detect(check_text3)
# string = check_text1
# lp = LineProfiler()
# lp_wrapper = lp(detect.__wrapped__)
# lp_wrapper(string)
# lp.print_stats()


# lp_wrapper = lprofiler(detect.__wrapped__)
# profile = LineProfiler(detect(dirty_text))
# # lp_wrapper()
# # lprofiler.print_stats()
# profile.print_stats()
