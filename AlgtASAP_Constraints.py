
from __future__ import division

# Uncomment the line below for readline support on interactive terminal
# import readline  

from pyparsing import Word, alphas, ParseException, Literal, CaselessLiteral \
, Combine, Optional, nums, Or, Forward, ZeroOrMore, StringEnd, alphanums,opAssoc
import math
import copy

# Debugging flag can be set to either "debug_flag=True" or "debug_flag=False"
debug_flag=True

exprStack = []
varStack  = []
NumUnit = 0
Result = []
StackAlap = []
TotalSteps = 0
TotalOperations = [0,0,0,0,0]


def pushFirst( str, loc, toks ):
    exprStack.append( toks[0] )

def assignVar( str, loc, toks ):
    varStack.append( toks[0] )

# define grammar
point = Literal('.')
plusorminus = Literal('+') | Literal('-')
number = Word(nums) 
integer = Combine( Optional(plusorminus) + number )
floatnumber = Combine( integer +
                       Optional( point + Optional(number) ) +
                       Optional( integer )
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
atom = ( ( floatnumber | integer | ident ).setParseAction(pushFirst) | 
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
def evaluateStack( s ):
  global NumUnit
  global TotalAdditions,TotalSubtrations,TotalMultiplications,Totaldivisions
  #Result.clear()
  op = s.pop()
  if op in "+-*/^":
    VarUnit = "Unit"+str(NumUnit)+ " "
    op2 = evaluateStack( s )
    op1 = evaluateStack( s )
    if ':' in op1 and ':' in op2:
        op1a,op1b,op1c,w1,w2=op1.split(":")
        op2a,op2b,op2c,w1,w2=op2.split(":")
        if int(op1c) > int(op2c):
           Step = 1 + int(op1c)
        else:
           Step = 1 + int(op2c)
        Temp = VarUnit + " : " + VarUnit + op + " " + op1a + " , " + op2a + " :" + str(Step) + ":" + op1a +":"+op2a
        Step = Step + 1
    elif ':' in op1:
        op1a,op1b,op1c,w1,w2=op1.split(":")
        Step = 1 + int(op1c)
        Temp = VarUnit + " : " + VarUnit + op + " " + op1a + " , " + op2 + " :" + str(Step) + ":" + op1a +":"+op2
    elif ':' in op2:
        op2a,op2b,op2c,w1,w2=op2.split(":")
        Step = 1 + int(op2c)
        Temp = VarUnit + " : " + VarUnit + op + " " + op1 + " , " + op2a + " :" + str(Step) + ":" + op1 +":"+op2a
    else:
        Step = 1
        Temp = VarUnit + " : " + VarUnit + op + " " + op1 + " , " + op2 + " :" + str(Step)  + ":" + op1 +":"+op2
        NumUnit = NumUnit + 1
    Result.append(Temp)
    if op == '+':
        TotalOperations[0] = TotalOperations[0] + 1
    elif op == '-':
        TotalOperations[1] = TotalOperations[1] + 1
    elif op == '*':
        TotalOperations[2] = TotalOperations[2] + 1
    elif op == '/':
        TotalOperations[3] = TotalOperations[3] + 1
	    



    return Temp
  else:
    return op 
    
def ShowResult():
	global TotalAdditions,TotalSubtrations,TotalMultiplications,Totaldivisions,NumUnit
	FinalAsap = ""
	print ("-----",Result)
	#StackAlap = copy.copy(Result)
	final = Result[-1]
	global TotalSteps
	temp1,temp2,TotalSteps,w1,w2 = final.split(':')
	#print (" ===",temp1," ", temp2," ", TotalSteps )
	for i in range(1,int(TotalSteps)+1):
		for j in Result:
			temp1,temp2,temp3,w1,w2 = j.split(':')
			if int(temp3) == i:
				#print (temp2)
				FinalAsap = FinalAsap + "\n" + temp2
		#print ("!")
		FinalAsap = FinalAsap + "\n" + "!"
	
	NumUnit=0
	FinalAsap = FinalAsap[1:-1]
	print ("=====================")
	print (FinalAsap)
	if TotalOperations[0] > 0:
		print (TotalOperations[0]," Additions")
	if TotalOperations[1] > 0:
		print (TotalOperations[1]," Subtractions") 
	if TotalOperations[2] > 0:
		print (TotalOperations[2]," Multiplications") 
	if TotalOperations[3] > 0:
		print (TotalOperations[3]," Divisions") 
	
	print ("=====================")
	
	
	return FinalAsap
	


# Recursive function that evaluates the stack
def AlgoALAP():
  global TotalSteps
  for smtnt in Result : 
      StackAlap.append(smtnt)
  ResAlap = []
  FinalAlap = ""
  #print (">>>>>>",TotalSteps,StackAlap)
  for smtnt in StackAlap : 
      deep=1
      dest,w1,Nstep,op1,op2 = smtnt.split(':')
      for smtnt2 in StackAlap:
          #print ("------",smtnt2)
          dest_2,w1_2,Nstep_2,op1_2,op2_2 = smtnt2.split(':')
          if int(Nstep) < int(Nstep_2):
             if dest in op1_2 or dest in op2_2:
                  #print ("*")
                  dest = dest_2
                  deep = deep + 1
      ResAlap.append(smtnt+":"+str(deep))
      #print (smtnt+":"+str(deep))
  
  
  i = int(TotalSteps)
  while i > 0:
    #print (i)
    for j in ResAlap:
        temp1,CodeString,w1,w2,w3,NumDpnd = j.split(':')
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
      
      # show result of parsing the input string
      if debug_flag: print (input_string, "->", L)
      if len(L)==0 or L[0] != 'Parse Failure':
        if debug_flag: print ("exprStack=", exprStack)
        Result.clear()
        evaluateStack(exprStack)
        ShowResult()
        AlgoALAP()
		
      else:
        print ('Parse Failure')
        print (err.line)
        print (" "*(err.column-1) + "^")
        print (err)
  
    # obtain new input string
    input_string = input("> ")
  
  # if user type 'quit' then say goodbye
  print ("Good bye!")


