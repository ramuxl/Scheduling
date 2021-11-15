#! /usr/bin/env python
# -*- coding: utf-8 -*-
#

from pyparsing import *
from Graph import *

word = Word(alphanums+"'.")
crt = OneOrMore(word)
op1 = OneOrMore(word)
op2 = OneOrMore(word)
comma = Literal(",")
symbol = oneOf("+ - / *")
greetee = OneOrMore(word)
endclk = oneOf("!")
endop = Literal(",")
operation = crt + symbol + op1 + comma + op2  | endclk



def TransfomerText(tests):
	print (tests)
	
	Val = ""
	dict2 = {}
	
	Sch = GraphScheduling()
	i=1
	cluster ="cluster"+str(i) 
	Sch.addClk(cluster)
	for t in tests.splitlines():
		print  (cluster)
		results = operation.parseString(t)
		print (results)
		
		if results[0] == '!':
		    Sch.endClk()
		    i+=1
		    cluster ="cluster"+str(i)
		    Sch.addClk(cluster)
		    dict1 = dict2.copy()
		else:
		    print ("=========>",results[0],results[1])
		    union = results[0] + str(i)
		    dict2[results[0]] = union			
		    try:
			    Or1 = dict1[results[2]]
			    
		    except:
			    op1 = results[2]+str(i)
			    Or1 = op1
			    Sch.g.node(Or1, results[2], shape='ellipse')
		    try:
			    Or2 = dict1[results[4]]
		    except:
			    op2 = results[4]+str(i)
			    Or2 = op2
			    Sch.g.node(Or2, results[4], shape='ellipse')
		    Sch.addNode(Or1, union)
		    Sch.addNode(Or2, union)
		    Sch.g.node(union, results[1], shape='circle')
		    
		    
		   
	Sch.g.node(union,results[1],shape='circle')
		
			
		
	Sch.endClk()
	print (Sch.g)
	Sch.render()
	return 1
	
	


if __name__ == '__main__':
	tests ="""\
        ADD1 - di7, di1
        ADD2 - di3, di5
        ADD3 - di6, di2
        !
        ADD1 + di4, ADD1
        ADD2 + di0, di8
        ADD3 + ADD2, ADD2
        ADD4 + ADD3, ADD3
        !
        ADD1 + ADD1, ADD2
        ADD2 + ADD3, ADD4
        !
        ADD1 - ADD2, ADD1  """
	TransfomerText(tests)
	
	
