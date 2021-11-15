#!/usr/bin/python

from graphviz import Digraph

class GraphScheduling():
	def __init__(self):
	   
	   self.g = Digraph('G', filename='GraphScheduling',format='png')
	
	def addNode(self, Op1, Op2):
		self.c.edge(Op1,Op2)
	def addClk(self, NumClk):
		self.c = Digraph(name=NumClk)
	def endClk(self,label,num):
		self.c.attr(label=label)
		self.c.attr(style='filled')
		if num % 2 == 0:
		    self.c.attr(color='darkorchid1')
		elif num % 3 == 0:
		    self.c.attr(color='aquamarine2')
		else:
		   self.c.attr(color='coral')
				
		self.g.subgraph(self.c,)
		
	def render(self):
		self.g.render()
		
def main():
	print ("MAIN")
			
if __name__ == '__main__':
    main()
