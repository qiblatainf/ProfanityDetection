from profanity_filter import ProfanityFilter
import spacy

def detect(string):
    nlp = spacy.load('en')
    pf = ProfanityFilter(nlps={'en': nlp})  
    nlp.add_pipe(pf.spacy_component, last=True)
    doc = nlp(string)
    print(doc._.is_profane)

