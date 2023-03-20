
from better_profanity import profanity



# @profile(precision=4)
def detect(string):
    result = profanity.contains_profanity(string)
    print(result)

# detect(check_text1)

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
