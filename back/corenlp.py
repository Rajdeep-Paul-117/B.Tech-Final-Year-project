import stanfordnlp
proxies = {'http': 'http://172.16.199.41:8080', 'https': 'http://172.16.199.41:8080'}
stanfordnlp.download('en')
nlp = stanfordnlp.Pipeline() 
doc = nlp("Barack Obama was born in Hawaii.  He was elected president in 2008.")
doc.sentences[0].print_dependencies()
# from stanfordcorenlp import StanfordCoreNLP

# nlp = StanfordCoreNLP(r'C:\Users\Acer User\Desktop\FInal year project\back\venv\Lib\site-packages\stanfordcorenlp')

# sentence = 'Guangdong University of Foreign Studies is located in Guangzhou.'
# print ('Named Entities:', nlp.ner(sentence))