import math
import string
import sys
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

translation_table = str.maketrans(string.punctuation+string.ascii_uppercase,
									" "*len(string.punctuation)+string.ascii_lowercase)
	
def get_words_from_line_list(text):
	
	text = text.translate(translation_table)
	word_list = text.split()
	
	return word_list

def count_frequency(word_list):
    D = {}
    sw = stopwords.words('english')
    X_set = {w for w in word_list if not w in sw}
    for new_word in X_set:
        if new_word in D:
            D[new_word] = D[new_word] + 1
        else:
            D[new_word] = 1
    return D

def word_frequencies_for_file(filename):
	word_list = get_words_from_line_list(filename)
	freq_mapping = count_frequency(word_list)
	return freq_mapping


def dotProduct(D1, D2):
	Sum = 0.0
	
	for key in D1:
		
		if key in D2:
			Sum += (D1[key] * D2[key])
			
	return Sum

def vector_angle(D1, D2):
    pi=22/7
    numerator = dotProduct(D1, D2)
    denominator = math.sqrt(dotProduct(D1, D1)*dotProduct(D2, D2))
    rad=math.acos(numerator / denominator)
    degree = rad*(180/pi)
    return degree


def documentSimilarity(filename_1, filename_2):

	sorted_word_list_1 = word_frequencies_for_file(filename_1)
	sorted_word_list_2 = word_frequencies_for_file(filename_2)
	distance = vector_angle(sorted_word_list_1, sorted_word_list_2)
	
	return "The distance between the documents is: % 0.6f (degree).\n NOTE: 0 degree means they are same documents, 90 degree means they are most disimilar"% distance