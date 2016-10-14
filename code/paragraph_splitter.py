from __future__ import division
import utils

class Splitter:
	def __init__(self, file_parser, model):
		self.file = file_parser
		self.model = model

	def split(self):
		sentencesList = self.file.getSentences()
		sentences = []
		for sentence in sentencesList :
			(sentence_dict, sentence_list) = utils.getWordsInSentence(sentence)
			sentences.append(set(sentence_list))

			self.model.add_vocab(sentence_dict)

		catch_phrasesList = self.file.getCatchPhrases()
		catch_phrases = []
		for cp in catch_phrasesList:
			(cp_dict, cp_list) = utils.getWordsInSentence(cp)
			catch_phrases.append(set(cp_list))

		batch_size = len(sentences) / len(catch_phrases)
		total_sentences = len(sentences)

		break_points = [(int(batch_size * i), int(batch_size * (i + 1)) - 1) for i in range(0, len(catch_phrases))]
		intersection_lengths = [[None for i in xrange(len(catch_phrases))] for j in xrange(len(sentences))]
		
		for i, bp in enumerate(break_points):
			for j in range(break_points[i][0], break_points[i][1]):
				intersection_lengths[j][i] = utils.getIntersectionLength(sentences[j], catch_phrases[i])

		not_change = False
		total_iterations = 20
		while not not_change :
			# find the interesting sentence for each sentence
			interesting_points = []
			for i, cp in enumerate(catch_phrases):
				current_sentences = sentences[break_points[i][0] : break_points[i][1] + 1]
				max_pos = None
				for j, sentence in enumerate(current_sentences) :
					j = j + break_points[i][0]
					if intersection_lengths[j][i] is None :
						intersection_lengths[j][i] = utils.getIntersectionLength(sentence, cp)
					current_val = intersection_lengths[j][i]
					if max_pos is None:
						max_pos = j
					if intersection_lengths[max_pos][i] < current_val:
						max_pos = j
				interesting_points.append(max_pos)
			change = False
			# find the new break_points and update change
			for i in range(0, len(catch_phrases) - 1) :
				midpoint = (interesting_points[i] + interesting_points[i + 1]) // 2
				
				if (break_points[i][1] != midpoint or break_points[i+1][0] != midpoint + 1):
					change = True

				break_points[i] = (break_points[i][0], midpoint)
				break_points[i + 1] = (midpoint + 1, break_points[i + 1][1])

			not_change = not change
			
			total_iterations = total_iterations - 1

			if total_iterations == 0 :
				break

		split_sentences = []
		split_points = []
		for i, bp in enumerate(break_points) :
			split_sentences.append( (sentencesList[bp[0] : bp[1]], catch_phrasesList[i]))
			v =  (bp[1] - bp[0] + 1) / total_sentences
			if i != 0 :
				v = v + split_points[-1]
			split_points.append(v)

		self.model.add_row(self.file.getDocumentSize(), split_points)

		return split_sentences

class DocumentSplitter:
	def __init__(self):
		self.splitPoints = {}
		self.vocab = {}

	def add_row(self, document_size, split_points):
		if document_size not in self.splitPoints:
			self.splitPoints[document_size] = [split_points]
		else :
			if len(self.splitPoints[document_size]) < len(split_points):
				self.splitPoints[document_size] = split_points

	def get_split_points(self, document_size):
		nearest = None
		nearestDistance = float(inf)
		for item, val in self.splitPoints.items():
			distance = (document_size - item) ** 2 **0.5
			if distance < nearestDistance:
				nearest = item
				nearestDistance = distance
			if distance == 0:
				break
		splitPointsData = self.splitPoints[nearest]
		return splitPointsData[0]

	def add_vocab(self, data_dict) :
		for key, val in data_dict.items() :
			if key in self.vocab :
				self.vocab[key] += val
			else :
				self.vocab[key] = val

	def get_vocab(self) :
		return self.vocab