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

	words = {}
	wordsList = []
	wordsSentence = sentence.split(" ")
	for word in wordsSentence :
		word = word.strip()
		word = stemmer.stem(lemmatizer.lemmatize(word))

		if word in words :
			words[word] += 1
		else :
			words[word] = 1

		if word not in stop :
			wordsList.append(word)
	return (words, wordsList)

def getIntersectionLength(wordsSentence, wordsCP) :
	sentenceSet = set(wordsSentence)
	cpSet = set(wordsCP)
	return len(sentenceSet.intersection(cpSet))

def convert2TFFormat(dataset) :
	article = "article=<d> <p> "
	for data in dataset :
		sentences = data[0]
		catch_phrase = data[1]

		for sentence in sentences :
			article = article + "<s>" + sentence + "</s> "

		article = article + "</p> </d> abstract=<d> <p> <s> " + catch_phrase[0] + " </s> </p> </d>"
	return article
