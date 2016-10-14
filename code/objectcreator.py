import os
import utils
from file_parser import FileParser
from paragraph_splitter import DocumentSplitter
from paragraph_splitter import Splitter

direc = "../dataset/trainingHalf/"
filelist = os.listdir(direc)

outputfile = open("data", "w")
vocabfile = open("vocab", "w")
training_data = ""
model = DocumentSplitter()
total = len(filelist)
i = 0
for eachfile in filelist[:1383]:
	i += 1
	print i
	fpObject = FileParser(direc + eachfile)
	splitter = Splitter(fpObject, model)

	split_data = splitter.split()
	training_data = utils.convert2TFFormat(split_data)
	outputfile.write(training_data.encode('utf-8') + "\n")

vocab = model.get_vocab()
for key,val in vocab.items() :
	vocabfile.write(key.encode("utf8") + " " + str(val) + "\n")
vocabfile.write("<p> 1\n")
vocabfile.write("</p> 1\n")
vocabfile.write("<s> 1\n")
vocabfile.write("</s> 1\n")
vocabfile.write("<d> 1\n")
vocabfile.write("</d> 1\n")
vocabfile.write("<UNK> 1\n")
vocabfile.write("<PAD> 1\n")
