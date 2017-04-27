import re
import math
def normalize(text):
	#return re.compile(r'\W+', re.UNICODE).split(text)
	re.sub('[^A-Za-z0-9]+', '', text)

def row_length(rownum):
	return math.ceil(math.sqrt(len(rownum)))
	
def divide_rows(text):
	#return text.split()
	#re.match(math.ceil(math.sqrt(len(text))), text , 'g')
	n = math.ceil(math.sqrt(len(text)))
	return[text[i:i+n] for i in range(0, len(text), n)]

def maker(text):
	output = []
	cols = len(text[0])
	for i in range(0, cols):
		word= ''
		for j in range(0, cols):
			try:
				word += text[j][i]
			except IndexError:
				pass
		output.append(word)
	return(output) 

def join(text):
	return " ".join(text)