import re
import math
def normalize(text):
	#return re.compile(r'\W+', re.UNICODE).split(text)
	re.sub('[^A-Za-z0-9]+', '', text)

def row_length(rownum):
	return math.ceil(math.sqrt(len(rownum)))
	
def divide_rows(text):
	re.match('.{1,' + math.ceil(math.sqrt(len(text))) + '}', 'g')