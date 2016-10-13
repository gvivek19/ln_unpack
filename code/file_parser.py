from bs4 import BeautifulSoup

class FileParser:
	def __init__(self, filename):
		self.file = open(filename)
		self.bs = BeautifulSoup(self.file, "lxml")
		self.lines = []
		self.parseSentences()
		self.cp = []
		self.parseCatchPhrases()
		
	def parseSentences(self) :
		raw_lines = self.bs.findAll('sentences')[0].contents[0].split("\n")
		for line in raw_lines:
			line = line.replace("\r", "")
			line = line.strip()
			if len(line) != 0 :
				self.lines.append(line)
	
	def parseCatchPhrases(self):
		raw_cp = self.bs.findAll("catchphrase")
		for cp in raw_cp:
			self.cp.append(cp.contents)
		
	def getCatchPhrases(self):
		return self.cp
	
	def getSentences(self) :
		return self.lines[:-9]
	
	def getName(self):
		return self.bs.findAll('name')[0].contents[0]
		
	def getURL(self):
		return self.bs.findAll('austlii')[0].contents[0]
