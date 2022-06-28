import cv2
class car:
	def __init__(self,mpdelname,year):
		self.mpdelname = mpdelname
		self.year = year
	def display(self):
		print(self.mpdelname,"", self.year)

c1=car("tpypta",2017) #c1 is object of car class
c1.display() # via object calling class's method
print(cv2.__version__)
