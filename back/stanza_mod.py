import stanza, json
proxies = {'http': 'http://172.16.199.41:8080', 'https': 'http://172.16.199.41:8080'}
stanza.download('en',proxies=proxies) # download English model
nlp = stanza.Pipeline(lang='en',proxies=proxies,processors='tokenize,ner')
doc = nlp("Los Angeles is capital of USA.")
print(type(doc.entities[0]))
# jsonStr = json.dumps(doc.entities)
# print(jsonStr)