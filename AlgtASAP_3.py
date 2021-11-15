
from __future__ import division

# Uncomment the line below for readline support on interactive terminal
# import readline  

from pyparsing import Word, alphas, ParseException, Literal, CaselessLiteral \
, Combine, Optional, nums, Or, Forward, ZeroOrMore, StringEnd, alphanums,opAssoc
import math
import copy
from AlgtASAP_2 import *

# Debugging flag can be set to either "debug_flag=True" or "debug_flag=False"
debug_flag=True


NumUnitR = 0

TotalOperationsR = [0,0,0,0,0]
CounterOperationsR = [0,0,0,0,0]
CentinelOperationsR = [1,1,1,1,1]
HuResource = [0,0,0,0,0]
dictStep = {}

def pushFirst( str, loc, toks ):
    exprStack.append( toks[0] )

def assignVar( str, loc, toks ):
    varStack.append( toks[0] )

# define grammar
point = Literal('.')
plusorminus = Literal('+') | Literal('-')
number = Word(nums) 
#integer = Combine( Optional(plusorminus) + number )
floatnumber = Combine( number +
                       Optional( point + Optional(number) ) +
                       Optional( number )
                     )

ident = Word(alphas,alphanums + '_') 

plus  = Literal( "+" )
minus = Literal( "-" )
mult  = Literal( "*" )
div   = Literal( "/" )
lpar  = Literal( "(" ).suppress()
rpar  = Literal( ")" ).suppress()
addop  = plus | minus
multop = mult | div
expop = Literal( "^" )
assign = Literal( "=" )

expr = Forward()
atom = ( ( floatnumber | number | ident ).setParseAction(pushFirst) | 
         ( lpar + expr.suppress() + rpar ) )
        
factor = Forward()
factor = atom + ZeroOrMore( ( expop + factor ).setParseAction( pushFirst ) )
        
term = factor + ZeroOrMore( ( multop + factor ).setParseAction( pushFirst ) )
expr << term + ZeroOrMore( ( addop + term ).setParseAction( pushFirst ) )
bnf = Optional((ident + assign).setParseAction(assignVar)) + expr

pattern =  bnf + StringEnd()

# map operator symbols to corresponding arithmetic operations

opn = { "+",
        "-",
        "*",
        "/",}



# Recursive function that evaluates the stack
def evaluateStackR( s , resourceConstraint ):
  #TotalOperations = [0,0,0,0,0]
  #CounterOperations = [0,0,0,0,0]
  #CentinelOperations = [1,1,1,1,1]
  global NumUnitR,TotalOperationsR
  global TotalAdditions,TotalSubtrations,TotalMultiplications,Totaldivisions,CounterOperationsR,CentinelOperationsR
  #Result.clear()
  op = s.pop()
  if op in "+-*/^":
    VarUnit = "Unit"+str(NumUnitR)+ " "
    op2 = evaluateStackR( s , resourceConstraint )
    op1 = evaluateStackR( s , resourceConstraint)
    if ':' in op1 and ':' in op2:
        op1a,op1b,op1c,w1,w2,s1=op1.split(":")
        op2a,op2b,op2c,w1,w2,s2=op2.split(":")
        if int(op1c) > int(op2c):
           Step = 1 + int(op1c)
        else:
           Step = 1 + int(op2c)
        Temp = VarUnit + " : " + VarUnit + op + " " + op1a + " , " + op2a + " :" + str(Step) + ":" + op1a +":"+op2a+":"+op
        Step = Step + 1
    elif ':' in op1:
        op1a,op1b,op1c,w1,w2,s1=op1.split(":")
        Step = 1 + int(op1c)
        Temp = VarUnit + " : " + VarUnit + op + " " + op1a + " , " + op2 + " :" + str(Step) + ":" + op1a +":"+op2+":"+op
    elif ':' in op2:
        op2a,op2b,op2c,w1,w2,s1=op2.split(":")
        Step = 1 + int(op2c)
        Temp = VarUnit + " : " + VarUnit + op + " " + op1 + " , " + op2a + " :" + str(Step) + ":" + op1 +":"+op2a+":"+op
    else:
        if op == "+":
            if resourceConstraint[0] > CounterOperationsR[0] and CentinelOperationsR[0] == 1:
                Step = CentinelOperationsR[0]
                CounterOperationsR[0] = CounterOperationsR[0] + 1
            #elif resourceConstraint[0]-1 > CounterOperations[0] and CentinelOperations[0] > 1:
            #    Step = CentinelOperations[0]
            #    CounterOperations[0] = CounterOperations[0] + 1
            elif  resourceConstraint[0] == 0:
                print ("NOT +")
                return "NOT"
            else:
                CounterOperationsR[0] = 1
                CentinelOperationsR[0] = CentinelOperationsR[0] + 1
                Step = CentinelOperationsR[0]
        elif op == "-":
            if resourceConstraint[1] > CounterOperationsR[1] and CentinelOperationsR[1] == 1:
                Step = CentinelOperationsR[1]
                CounterOperationsR[1] = CounterOperationsR[1] + 1
            #elif resourceConstraint[1]-1 > CounterOperationsR[1] and CentinelOperationsR[1] > 1:
            #    Step = CentinelOperationsR[1]
            #    CounterOperationsR[1] = CounterOperationsR[1] + 1
            elif  resourceConstraint[1] == 0:
                print ("NOT -")
                return "NOT"
            else:
                CounterOperationsR[1] = 1
                CentinelOperationsR[1] = CentinelOperationsR[1] + 1
                Step = CentinelOperationsR[1]
        elif op == "*":
            if resourceConstraint[2] > CounterOperationsR[2] and CentinelOperationsR[2] == 1:
                Step = CentinelOperationsR[2]
                CounterOperationsR[2] = CounterOperationsR[2] + 1
            #elif resourceConstraint[2]-1 > CounterOperationsR[2] and CentinelOperationsR[2] > 1:
            #    Step = CentinelOperationsR[2]
            #    CounterOperationsR[2] = CounterOperationsR[2] + 1
            elif  resourceConstraint[2] == 0:
                print ("NOT *")
                return "NOT"
            else:
                CounterOperationsR[2] = 1
                CentinelOperationsR[2] = CentinelOperationsR[2] + 1
                Step = CentinelOperationsR[2]
        elif op == "/":
            if resourceConstraint[3] > CounterOperationsR[3] and CentinelOperationsR[3] == 1:
                Step = CentinelOperationsR[3]
                CounterOperationsR[3] = CounterOperationsR[3] + 1
            #elif resourceConstraint[3]-1 > CounterOperationsR[3] and CentinelOperationsR[3] > 1:
            #    Step = CentinelOperationsR[3]
            #    CounterOperationsR[3] = CounterOperationsR[3] + 1
            elif  resourceConstraint[3] == 0:
                print ("NOT /")
                return "NOT"
            else:
                CounterOperationsR[3] = 1
                CentinelOperationsR[3] = CentinelOperationsR[3] + 1
                Step = CentinelOperationsR[3]
        			 
        Temp = VarUnit + " : " + VarUnit + op + " " + op1 + " , " + op2 + " :" + str(Step)  + ":" + op1 +":"+op2+":"+op
        NumUnitR = NumUnitR + 1
    Result.append(Temp)
    if op == '+':
        TotalOperationsR[0] = TotalOperationsR[0] + 1
    elif op == '-':
        TotalOperationsR[1] = TotalOperationsR[1] + 1
    elif op == '*':
        TotalOperationsR[2] = TotalOperationsR[2] + 1
    elif op == '/':
        TotalOperationsR[3] = TotalOperationsR[3] + 1
	    



    return Temp
  else:
    return op 

def ShowResultR():
	global TotalAdditions,TotalSubtrations,TotalMultiplications,Totaldivisions,NumUnitR,TotalOperationsR
	FinalAsap = ""
	print ("-----",Result)
	#StackAlap = copy.copy(Result)
	final = Result[-1]
	global TotalSteps,HuResource
	temp1,temp2,TotalSteps,w1,w2,sim = final.split(':')
	print (" ===================================",temp1," ", temp2," ", TotalSteps )
	for i in range(1,int(TotalSteps)+1):
		for j in Result:
			temp1,temp2,temp3,w1,w2,sim = j.split(':')
			if int(temp3) == i:
				#print (temp2)
				FinalAsap = FinalAsap + "\n" + temp2
		#print ("!")
		FinalAsap = FinalAsap + "\n" + "!"
	
	NumUnitR=0
	FinalAsap = FinalAsap[1:-1]
	print ("=====================")
	print (FinalAsap)
	if TotalOperationsR[0] > 0:
		print (TotalOperationsR[0]," Additions")
	if TotalOperationsR[1] > 0:
		print (TotalOperationsR[1]," Subtractions") 
	if TotalOperationsR[2] > 0:
		print (TotalOperationsR[2]," Multiplications") 
	if TotalOperationsR[3] > 0:
		print (TotalOperationsR[3]," Divisions") 
	
	print ("=====================")
	print (CounterOperationsR)
	print (CentinelOperationsR)
	print (TotalOperationsR)
	
	CentinelOperationsR[0]=1
	CentinelOperationsR[1]=1
	CentinelOperationsR[2]=1
	CentinelOperationsR[3]=1
	
	CounterOperationsR[0]=0
	CounterOperationsR[1]=0
	CounterOperationsR[2]=0
	CounterOperationsR[3]=0
	
	return FinalAsap
 
# Recursive function that evaluates the stack
def AlgoALAPR(resourceConstraint):
  #TotalOperationsR = [0,0,0,0,0]
  CounterOperationsR = [0,0,0,0,0]
  #CentinelOperationsR = [1,1,1,1,1]
  global TotalSteps,HuResource,TotalOperationsR
  for smtnt in Result : 
      StackAlap.append(smtnt)
  ResAlap = []
  FinalAlap = ""
  #print (">>>>>>",TotalSteps,StackAlap)
  for smtnt in StackAlap : 
      deep=1
      dest,w1,Nstep,op1,op2,simb = smtnt.split(':')
      for smtnt2 in StackAlap:
          #print ("------",smtnt2)
          dest_2,w1_2,Nstep_2,op1_2,op2_2,simb = smtnt2.split(':')
          if int(Nstep) < int(Nstep_2):
             if dest in op1_2 or dest in op2_2:
                  #print ("*")
                  dest = dest_2
                  deep = deep + 1
      ResAlap.append(smtnt+":"+str(deep))
      print (smtnt+":"+str(deep))
  
  
  i = int(TotalSteps)
  while i > 0:
    #print (i)
    for idx, j in enumerate(ResAlap):
        temp1,CodeString,w1,w2,w3,simb,NumDpnd = j.split(':')
        if int(NumDpnd) == i:
           
           
           if simb == "+":
               if resourceConstraint[0] > CounterOperationsR[0]:
                   CounterOperationsR[0] = CounterOperationsR[0] + 1
                   #FinalAlap = FinalAlap + "\n" + CodeString
               elif  resourceConstraint[0] == 0:
                   print ("NOT +")
                   HuResource[0] = HuResource[0] +1
                   return "NOT"
               else:
                   ResAlap[idx] = temp1+":"+CodeString+":"+w1+":"+w2+":"+w3+":"+simb+":"+str(i+1)
           elif simb == "-":
               if resourceConstraint[1] > CounterOperationsR[1]:
                   CounterOperationsR[1] = CounterOperationsR[1] + 1
                   #FinalAlap = FinalAlap + "\n" + CodeString
               elif  resourceConstraint[1] == 0:
                   print ("NOT -")
                   HuResource[1] = HuResource[1] +1
                   return "NOT"
               else:
                   print ("VVVVVVVVVVV",temp1+":"+CodeString+":"+w1+":"+w2+":"+w3+":"+simb+":"+str(i+1))
                   ResAlap[idx] = temp1+":"+CodeString+":"+w1+":"+w2+":"+w3+":"+simb+":"+str(i+1)
           elif simb == "*":
               if resourceConstraint[2] > CounterOperationsR[2] and CentinelOperationsR[2] == 1:
                   Step = CentinelOperationsR[2]
                   CounterOperationsR[2] = CounterOperationsR[2] + 1
               elif resourceConstraint[2]-1 > CounterOperationsR[2] and CentinelOperationsR[2] > 1:
                   Step = CentinelOperationsR[2]
                   CounterOperationsR[2] = CounterOperationsR[2] + 1
               elif  resourceConstraint[2] == 0:
                   print ("NOT *")
                   HuResource[2] = HuResource[2] +1
                   return "NOT"
               else:
                   CounterOperationsR[2] = 1
                   CentinelOperationsR[2] = CentinelOperationsR[2] + 1
                   Step = CentinelOperationsR[2]
           elif simb == "/":
               if resourceConstraint[3] > CounterOperationsR[3] and CentinelOperationsR[3] == 1:
                   Step = CentinelOperationsR[3]
                   CounterOperationsR[3] = CounterOperationsR[3] + 1
               elif resourceConstraint[3]-1 > CounterOperationsR[3] and CentinelOperationsR[3] > 1:
                   Step = CentinelOperationsR[3]
                   CounterOperationsR[3] = CounterOperationsR[3] + 1
               elif  resourceConstraint[3] == 0:
                   print ("NOT /")
                   HuResource[3] = HuResource[3] +1
                   return "NOT"
               else:
                   CounterOperationsR[3] = 1
                   CentinelOperationsR[3] = CentinelOperationsR[3] + 1
                   Step = CentinelOperationsR[3]
           
           			
           ###FinalAlap = FinalAlap + "\n" + CodeString
           #print (CodeString)
    CounterOperationsR = [0,0,0,0,0]
    i=i-1
    #FinalAlap = FinalAlap + "\n" + "!"
  i = int(TotalSteps)
  while i > 0:
    #print (i)
    for j in ResAlap:
        temp1,CodeString,w1,w2,w3,simb,NumDpnd = j.split(':')
        if int(NumDpnd) == i:
           FinalAlap = FinalAlap + "\n" + CodeString
           #print (CodeString)
    i=i-1
    FinalAlap = FinalAlap + "\n" + "!"  
  FinalAlap = FinalAlap[1:-1]
  print ("**********************************")
  print (FinalAlap)
  print ("**********************************")
  ResAlap.clear()
  StackAlap.clear()
  return FinalAlap
  
  
 

		  
		  
  
  
    
if __name__ == '__main__':
  # input_string
  input_string=''
  NumberofClk = 8
  NumberUnit = [1,1,1,1]
  
  # Display instructions on how to quit the program
  print ("Type in the string to be parse or 'quit' to exit the program")
  input_string = input("> ")
  
  while input_string != 'quit':
    # Start with a blank exprStack and a blank varStack
    exprStack = []
    varStack  = []
  
    if input_string != '':
      # try parsing the input string
      try:
        L=pattern.parseString( input_string )
      except ParseException as err:
        L=['Parse Failure',input_string]
      SpecialFunction()
      # show result of parsing the input string
      if debug_flag: print (input_string, "->", L)
      if len(L)==0 or L[0] != 'Parse Failure':
        if debug_flag: print ("exprStack=", exprStack)
        Result.clear()
        RES=evaluateStackR(exprStack,NumberUnit)
        if RES != "NOT":
            ShowResultR()
        #ShowResult()a+b+c+d+f+g
        #AlgoALAP()
        print ("##########################################################################")
        AlgoALAPR(NumberUnit)
        #Result.clear()
        #evaluateStack(exprStack)
        
        #ShowResulConstraint("Resource constrained", NumberofClk,NumberUnit)
        #AlgoALAPConstraint("Time constrained", NumberofClk,NumberUnit)
      else:
        print ('Parse Failure')
        print (err.line)
        print (" "*(err.column-1) + "^")
        print (err)
  
    # obtain new input string
    input_string = input("> ")
  
  # if user type 'quit' then say goodbye
  print ("Good bye!")


