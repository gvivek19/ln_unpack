from bs4 import BeautifulSoup

class FileParser:
	def __init__(self, filename):
		self.file = open(filename)
		self.bs = BeautifulSoup(self.file, "lxml")
		self.lines = []
		self.docSize = 0
		self.parseSentences()
		self.cp = []
		self.parseCatchPhrases()
		
	def parseSentences(self) :
		startNo = 1
		raw_lines = self.bs.findAll('sentences')[0].contents[0].split("\n")
		for line in raw_lines:
			line = line.replace("\r", "")
			line = line.strip()
			if len(line) != 0 :
				self.lines.append(line)
				self.docSize += len(line.split(" "))
	
	def parseCatchPhrases(self):
		raw_cp = self.bs.findAll("catchphrase")
		for cp in raw_cp:
			self.cp.append(cp.contents[0])
		
	def getCatchPhrases(self):
		return self.cp
	
	def getSentences(self) :
		return self.lines[:-9]
	
	def getName(self):
		return self.bs.findAll('name')[0].contents[0]
		
	def getURL(self):
		return self.bs.findAll('austlii')[0].contents[0]

	def getNumSentences(self):
		return len(self.sentences)

	def getNumCP(self):
		return len(self.cp)

	def getDocumentSize(self):
		return self.docSize
