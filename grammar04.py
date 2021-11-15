#!/usr/bin/python
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
	outcomeend=""
	Sch = GraphScheduling()
	i=1
	cluster ="cluster"+str(i) 
	Sch.addClk(cluster)
	Exe = 0
	for t in tests.splitlines():
		print  (cluster)
		
		try:
		   results = operation.parseString(t)
		except:
			return False
			
		print (results)
		
		if results[0] == '!':
		    label= "Clk "+ str(i)
		    Sch.endClk(label,i)
		    i+=1
		    cluster ="cluster"+str(i)
		    Sch.addClk(cluster)
		    dict1 = dict2.copy()
		    Exe = 0
		else:
		    print ("=========>",results[0],results[1])
		    unit = results[0] + str(i)
		    outcome = "outcome"+unit
		    
		    dict2[results[0]] = outcome	
		    	
		    try:
			    Or1 = dict1[results[2]]
			    Out1= "outcome"+Or1
			    #Sch.addNode(Or1,Out1,str(arrowhead='none'))
			    Sch.c.edge(Or1,Out1,arrowhead='none')
			    Sch.g.node(Out1, shape='diamond',style='filled',label='',height='.1',width='.1' )
			    
		    except:
			    op1 = results[2]+str(i)
			    Out1 = op1
			    Sch.g.node(Out1, results[2], shape='ellipse')
			    Sch.g.node_attr.update(style='filled', color='white')
		    try:
			    Or2 = dict1[results[4]]
			    Out2= "outcome"+Or2
			    if Out2 != Out1:
			        #Sch.addNode(Or2,Out2)
			        Sch.c.edge(Or2,Out2,arrowhead='none')
			        Sch.g.node(Out2, shape='diamond',style='filled',label='',height='.1',width='.1' )
		    except:
			    op2 = results[4]+str(i)
			    Out2 = op2
			    Sch.g.node(Out2, results[4], shape='ellipse')
			    Sch.g.node_attr.update(style='filled', color='white')
		    Sch.addNode(Out1, unit)
		    Sch.addNode(Out2, unit)
		    
		    Sch.g.node(unit, results[1], shape='circle')
		    #Sch.addNode(unit, outcome)
		    Sch.c.edge(unit,outcome,arrowhead='none')
		    outcomeend= outcome
		    Sch.g.node(outcome, shape='diamond',style='filled',label='',height='.1',width='.1' )
		    
		    
		   
	Sch.g.node(unit,results[1],shape='circle')
	label = "Clk " + str(i)
	Sch.endClk(label,i)
	EndNode = "End"
	Sch.g.edge(outcomeend, EndNode)
	Sch.g.attr(style='filled')
	Sch.g.node_attr.update(color='darkolivegreen1')
	Sch.g.node(EndNode,shape='Msquare')
	
	
	
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
	
	
