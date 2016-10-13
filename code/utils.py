import nltk
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

#nltk.download()

def tokenize(sentence):
	tokens = []
	words = sentence.split(" ")
	for word in words :
		word = word.strip()
		tokens.add(word)
	return tokens

def getWordsInSentence(sentence) :
	lemmatizer = WordNetLemmatizer()
	stemmer = PorterStemmer()
	stop = set(stopwords.words('english'))

	words = []
	wordsSentence = sentence.split(" ")
	for word in wordsSentence :
		word = word.strip()
		if word.lower() not in stop:
			words.append(stemmer.stem(lemmatizer.lemmatize(word)))
	return words

def getIntersectionLength(wordsSentence, wordsCP) :
	sentenceSet = set(wordsSentence)
	cpSet = set(wordsCP)
	return len(sentenceSet.intersection(cpSet))

