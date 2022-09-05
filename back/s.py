# import nltk
# # nltk.download('punkt')
# # nltk.download('averaged_perceptron_tagger')
# sentence = """At eight o'clock on Thursday morning
# ... Arthur didn't feel very good."""
# tokens = nltk.word_tokenize(sentence)
# print(tokens)
# tagged = nltk.pos_tag(tokens)
# tagged[0:6]
# print(tagged)
import stanza_mod
proxies = {'http': 'http://172.16.199.41:8080', 'https': 'http://172.16.199.41:8080'}
stanza_mod.download('en',proxies=proxies) # download English model
nlp = stanza_mod.Pipeline(lang='en',proxies=proxies)
doc = nlp("Los Angeles is capital of USA.")
print(doc)
print(doc.entities)

# pip install --proxy http://172.16.199.41:8080 stanza

####################  Spacy   ##################
# import spacy
# from spacy import displacy
# from collections import Counter
# # spacy.download(en_core_web_sm)
# import en_core_web_sm
# nlp = en_core_web_sm.load()
# doc = nlp('New Delhi is capital of India')
# print([(X.text, X.label_) for X in doc.ents])
####################  Spacy   ##################

# python -m spacy download en_core_web_sm
# import stanza
# nlp = stanza.Pipeline(lang='en', processors='tokenize,ner')
# doc = nlp("Chris Manning teaches at Stanford University. He lives in the Bay Area.")
# print(*[f'entity: {ent.text}\ttype: {ent.type}' for ent in doc.ents], sep='\n')