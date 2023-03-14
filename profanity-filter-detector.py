from profanity_filter import ProfanityFilter
import spacy
from memory_profiler import profile
from line_profiler import LineProfiler

check_text = "That wh0re gave m3 a very good H4nd j0b hehe"
nlp = spacy.load('en')
pf = ProfanityFilter(nlps={'en': nlp})  # reuse spacy Language (optional)
nlp.add_pipe(pf.spacy_component, last=True)

@profile(precision=4)
def detect(string):
    doc = nlp(string)
    print(doc._.is_profane)

detect(check_text)