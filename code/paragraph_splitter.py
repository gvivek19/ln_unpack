class Splitter:
	def __init__(self, file_parser, model):
		self.file = file_parser
		self.model = model

	def split(self):
		pass

class DocumentSplitter:
	def __init__(self):
		self.splitPoints = {}

	def add_row(self, document_size, split_points):
		if document_size not in self.splitPoints:
			self.splitPoints[document_size] = split_points
		else:
			self.splitPoints[document_size] = self.splitPoints[document_size].append(split_points)

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
		max_length = 0
		splitPoints = []

		for sp in splitPointsData:
			if len(sp) > max_length :
				max_length = len(sp)
				splitPoints = sp
		return splitPoints