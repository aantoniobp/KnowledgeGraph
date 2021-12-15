import spacy
from spacy.matcher import Matcher
nlp = spacy.load('en_core_web_sm')

matcher = Matcher(nlp.vocab)
pattern = [{"LOWER": "hello"}, {"LOWER": "world"}]
matcher.add("Hello World", [pattern])
doc = nlp("hello WORLD")
matches = matcher(doc)
print(matches)  
print(len(matches))
print(doc[matches[0][1]:matches[0][2]])
