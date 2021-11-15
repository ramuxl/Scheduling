
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

#funtion that changes similar prioritis 
def SpecialFunction ():
    Max = len(exprStack)
    print(">>>> " ,Max)
    print(">>>> " ,exprStack)
    i = 0	
    while i < Max-1:
        if exprStack[i] in "+-*/" :
            #print ("change")
            #print (exprStack[i-1])
            #print (exprStack[i])
            #print (exprStack[i-2])
            if exprStack[i-1] not in  "+-*/"  and exprStack[i] == exprStack[i-2] and  exprStack[i+1] not in "+-*/" :
               temp1=exprStack[i]
               temp2=exprStack[i+1]
               exprStack[i]=temp2
               exprStack[i+1]=temp1
        i=i+1
    #Second Part of the function
    
    ptt1=""
    ptt2=""
    
    numPtt = 2
    
    while numPtt < (Max/4):
        revIns=0
        revInsBool = True
        evenNumber = 0
        print ("********************************************\n",numPtt)
        i = 0
        NP = 0
        while i < Max:
           if exprStack[i] in "+-*/" :
               j=1
               RestBool = True
               while j < numPtt:
                   RestBool = RestBool and exprStack[i-j] in "+-*/"
                   #print ("=======",RestBool, " ", i," ",j," ",exprStack[i-j])
                   j=j+1
               if RestBool:
                   NP = NP +1 
               try:
                   if  RestBool and exprStack[i+1] not in "+-*/" and exprStack[i-numPtt] not in "+-*/" and NP >= 2:
                       if revIns == 0:
                           print(">>>>>>>>>>>>>>>>>>>>><remove ", i)
                           revIns = revIns +1
                           evenNumber = evenNumber + 1
                       else:
                           print(">>>>>>>>>>>>>>>>>>>>><Insert ", i)
                           revIns=0
                           evenNumber = evenNumber + 1
                   if revIns == 1 and i == Max-1:
                           print(">>>>>>>>>>>>>>>>>>>>><Insert ", i)
                           revIns=0
                           evenNumber = evenNumber + 1
               except:
                   if  RestBool and exprStack[i-numPtt] not in "+-*/" and NP >= 2:
                       if revIns == 0 and i != Max-1:
                           print("---------------------><remove ", i, Max)
                           revIns = revIns +1
                           evenNumber = evenNumber + 1
                       elif revIns == 1 and i == Max-1:
                           print("--------------------><Insert ", i)
                           revIns=0
                           evenNumber = evenNumber + 1
                   if revIns == 1 and i == Max-1:
                           print("--------------------><Insert ", i)
                           revIns=0
                           evenNumber = evenNumber + 1
               print ("-->",evenNumber)
                                        
				   		    
           i = i+1
        
        
        
        
        revInsBool = True
        print ("===============================================\n",numPtt)
        i = 0
        NP = 0
        while i < Max:
           if exprStack[i] in "+-*/":
               j=1
               RestBool = True
               while j < numPtt:
                   RestBool = RestBool and exprStack[i-j] in "+-*/"
                   #print ("=======",RestBool, " ", i," ",j," ",exprStack[i-j])
                   j=j+1 
               if RestBool:
                   NP = NP +1
               
               print ("-->",evenNumber)
               if evenNumber%2 == 0:
                   print ("Action")
                   try:
                       if  RestBool and exprStack[i+1] not in "+-*/" and exprStack[i-numPtt] not in "+-*/" and NP >= 2 :
                           if revInsBool:
                               print("*******><remove ", i)
                               TempVal = exprStack[i]
                               del exprStack[i]
                               revInsBool = False   
                           else:
                               print("*******><Insert ", i)
                               exprStack.insert(i, TempVal)
                               revInsBool=True
                       if revInsBool == False and i == Max-2:
                           print("*******><Insert ", i)
                           exprStack.insert(i, TempVal)
                           revInsBool=True
                   except:
                       if  RestBool and exprStack[i-numPtt] not in "+-*/" and NP >= 2 :
                           if revInsBool and i != Max-1 :
                               print("*******><remove ", i)
                               TempVal = exprStack[i]
                               del exprStack[i]
                               revInsBool = False   
                           elif revInsBool == False:
                               print("*******><Insert ", i)
                               exprStack.insert(i, TempVal)
                               revInsBool=True
                       if revInsBool == False and i == Max-2:
                               print("*******><Insert ", i)
                               exprStack.insert(i, TempVal)
                               revInsBool=True
				   		    
           i = i+1
        
        print ("exprStack=", exprStack)
        numPtt=numPtt+1

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
        Step = 1
        Temp = VarUnit + " : " + VarUnit + op + " " + op1 + " , " + op2 + " :" + str(Step)  + ":" + op1 +":"+op2+":"+op
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
	temp1,temp2,TotalSteps,w1,w2,sim = final.split(':')
	#print (" ===",temp1," ", temp2," ", TotalSteps )
	for i in range(1,int(TotalSteps)+1):
		for j in Result:
			temp1,temp2,temp3,w1,w2,sim = j.split(':')
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
      #print (smtnt+":"+str(deep))
  
  
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
  #ResAlap.clear()
  while ResAlap:
    ResAlap.pop()
  #StackAlap.clear()
  while StackAlap:
    StackAlap.pop()
  return FinalAlap
  
  
 
def ShowResulConstraint( constraint , timeConstraint, resourceConstraint ):
	global TotalAdditions,TotalSubtrations,TotalMultiplications,Totaldivisions,NumUnit
	FinalAsap = ""
	print ("********",Result)
	print (constraint)
	if constraint == "Time constrained":
	    #StackAlap = copy.copy(Result)
	    final = Result[-1]
	    
	        
	    global TotalSteps
	    print ("++++> " , final)
	    temp1,temp2,TotalSteps,w1,w2,w3 = final.split(':')
	    print ("<<<<<<<<< ", TotalSteps,  timeConstraint)
	    if int(TotalSteps) > timeConstraint:
	        msg = "It's impossible to solve in that number of clks steps"
	        print (msg)
	        return msg
	    else:
	        #print (" ===",temp1," ", temp2," ", TotalSteps )
	        for i in range(1,int(TotalSteps)+1):
	           for j in Result:
	                temp1,temp2,temp3,w1,w2,w3 = j.split(':')
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
    
#	elif constraint == "Resource constrained":
		
#	    print ("Algo Resource constrained//////")
#	    print (resourceConstraint)
#	    dicti = {}	
	    #for i in Result:
	    #    print (i)
	    #print ("<<<< " ,TotalSteps)
#	    print ("****************************************************")
#	    for i in range(1,int(TotalSteps)+1):
#	        print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>> ",i)
#	        usedOperations = [0,0,0,0,0]
#	        for k,j in enumerate(Result):
	            
#	            temp1,temp2,temp3,w1,w2,simb = j.split(':')
#	            if int(temp3) == i:
#	                print ("<<<<<<<<<<<<<<<<< PROCESS LINE")
#	                print ("---->", k," ",j)
#	                print ("/\\",resourceConstraint[0], usedOperations[0])
#	                simb = simb.replace(" ","")
#	                print ("*******",simb)
#	                if simb == '+':
#	                    if resourceConstraint[0] > usedOperations[0]:
#	                        print ("/\/\/\/\> ",resourceConstraint[0], usedOperations[0])
	                        	                        
#	                        if w1 in dicti or w2 in dicti:
	                            
#	                            try:
#	                                newValSetp1 = dicti[w1]
#	                            except:
#	                                newValSetp1 = 0
	                                
#	                            try:
#	                                newValSetp2 = dicti[w2]
#	                            except:
#	                                newValSetp2 = 0
	                             
#	                            if newValSetp1 > newValSetp2:
#	                                newValSetp = newValSetp1
#	                            else:
#	                                newValSetp = newValSetp1
	                            #newValSetp = newValSetp + 1
	                            #print (";;;;;> ",resourceConstraint[0], usedOperations[0],newValSetp )
	                            #print (";;;;;> ", Result[k])
	                            #Result[k]=temp1+" : "+temp2+" : "+str(newValSetp) +" : "+w1+" : "+w2+" : "+simb
	                            #print (";;;;;> ", Result[k])
	                            #dicti[temp1] = newValSetp
#	                        usedOperations[0]= usedOperations[0] + 1 
#	                    else:
	                        #if w1 in dicti or w2 in dicti:
	                        #    try:
	                        #        newValSetp1 = dicti[w1]
	                        #    except:
	                        #        newValSetp1 = 0
	                                
	                        #    try:
	                        #        newValSetp2 = dicti[w2]
	                        #    except:
	                        #        newValSetp2 = 0
	                                
	                        #    if newValSetp1 > newValSetp2:
	                        #        newValSetp = newValSetp1
	                        #    else:
	                        #        newValSetp = newValSetp1
	                        #    newValSetp = newValSetp + 1
	                        #    print ("=-=-=-> ",resourceConstraint[0], usedOperations[0])
	                        #    print ("=-=-=-> ", Result[k])
	                        #    Result[k]=temp1+" : "+temp2+" : "+str(newValSetp) +" : "+w1+" : "+w2+" : "+simb
	                        #    print ("=-=-=-> ", Result[k])
	                        #else:    
#	                        newValSetp = int(temp3) + 1
#	                        print ("#####> ",resourceConstraint[0], usedOperations[0])
#	                        print ("#####> ", Result[k])
#	                        Result[k]=temp1+" : "+temp2+" : "+str(newValSetp) +" : "+w1+" : "+w2+" : "+simb
#	                        print ("#####> ", Result[k])
#	                        dicti[temp1] = newValSetp
#	                    print ("/\\",resourceConstraint[0], usedOperations[0])
	                		
#	                elif simb == '-':
#	                    if resourceConstraint[0] >= usedOperations[0]:
#	                        usedOperations[0]= usedOperations[0] + 1
#	                    else:
#	                        newValSetp = int(temp3) + 1
#	                        Result[k]=temp1+" : "+temp2+" : "+newValSetp +" : "+w1+" : "+w2+" : "+simb
						
#	                elif simb == '*':
#	                    if resourceConstraint[0] >= usedOperations[0]:
#	                        usedOperations[0]= usedOperations[0] + 1
#	                    else:
#	                        newValSetp = int(temp3) + 1
#	                        Result[k]=temp1+" : "+temp2+" : "+newValSetp +" : "+w1+" : "+w2+" : "+simb
					
#	                elif simb == '/':
#	                    if resourceConstraint[0] >= usedOperations[0]:
#	                        usedOperations[0]= usedOperations[0] + 1
#	                    else:
#	                        newValSetp = int(temp3) + 1
#	                        Result[k]=temp1+" : "+temp2+" : "+newValSetp +" : "+w1+" : "+w2+" : "+simb
	                #FinalAsap = FinalAsap + "\n" + temp2
#	                print ("<<<<<<<<<<<<<<<<<< PROCESS LINE\n\n")
#	        usedOperations[0] = 0
#	    print ("****************************************************")
	                
	            #j= j+1
	        #FinalAsap = FinalAsap + "\n" + "!"
#	    final = Result[-1]
#	    temp1,temp2,TotalStepsNew,w1,w2,sim = final.split(':')
#	    for i in range(1,int(TotalStepsNew)+1):
#	        for j in Result:
#	            temp1,temp2,temp3,w1,w2,sim = j.split(':')
#	            if int(temp3) == i:
				       #print (temp2)
#	                FinalAsap = FinalAsap + "\n" + temp2
		        #print ("!")
#	        FinalAsap = FinalAsap + "\n" + "!"
	
#	    NumUnit=0
#	    FinalAsap = FinalAsap[1:-1]
#	    print ("=====================")
#	    print (FinalAsap)
#	    print ("=====================")
	        
#	        NumUnit=0
#	        FinalAsap = FinalAsap[1:-1]
#	        print ("=====================")
#	        print (FinalAsap)
#	        if TotalOperations[0] > 0:
#		        print (TotalOperations[0]," Additions")
#	        if TotalOperations[1] > 0:
#		        print (TotalOperations[1]," Subtractions") 
#	        if TotalOperations[2] > 0:
#		        print (TotalOperations[2]," Multiplications") 
#	        if TotalOperations[3] > 0:
#	            print (TotalOperations[3]," Divisions") 
#	        print ("=====================")
	
	return FinalAsap
	


# Recursive function that evaluates the stack
def AlgoALAPConstraint( constraint , timeConstraint, resourceConstraint ):
  global TotalSteps
  minTotalSteps = TotalSteps
  ResAlap = []
  FinalAlap = ""
  TotalSteps = int(timeConstraint)
  if constraint == "Time constrained":
      print ("0403043040430430404 ",minTotalSteps,TotalSteps)	  
      if int(minTotalSteps) > int(TotalSteps):
          msg = "It's impossible to solve in that number of clks steps"
          print (msg)
          return msg
	        
      for smtnt in Result : 
          StackAlap.append(smtnt)
      
      #print (">>>>>>",TotalSteps,StackAlap)
      for smtnt in StackAlap : 
          deep=1
          print ("====> ", smtnt)
          dest,w1,Nstep,op1,op2,sim = smtnt.split(':')
          for smtnt2 in StackAlap:
              #print ("------",smtnt2)
              dest_2,w1_2,Nstep_2,op1_2,op2_2,sim = smtnt2.split(':')
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
              print ("====> ", j)
              temp1,CodeString,w1,w2,w3,w4,NumDpnd = j.split(':')
              if int(NumDpnd) == i:
                  FinalAlap = FinalAlap + "\n" + CodeString
                  #print (CodeString)
          i=i-1
          FinalAlap = FinalAlap + "\n" + "!"
      
      FinalAlap = FinalAlap[1:-1]
      
      print ("**********************************")
      print (FinalAlap)
      print ("**********************************")
  elif constraint == "Resource constrained":
      print ("!Algo Resource constrained!!!!!")
  
  ResAlap.clear()
  StackAlap.clear()
  return FinalAlap
		  
		  
  
  
    
if __name__ == '__main__':
  # input_string
  input_string=''
  NumberofClk = 8
  NumberUnit = [2,1,1,1]
  
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
        evaluateStack(exprStack)
        #ShowResult()
        #AlgoALAP()
        print ("##########################################################################")
        #Result.clear()
        #evaluateStack(exprStack)
        #ShowResult()
        ShowResulConstraint("Time constrained", NumberofClk,NumberUnit)
        AlgoALAPConstraint("Time constrained", NumberofClk,NumberUnit)
      else:
        print ('Parse Failure')
        print (err.line)
        print (" "*(err.column-1) + "^")
        print (err)
  
    # obtain new input string
    input_string = input("> ")
  
  # if user type 'quit' then say goodbye
  print ("Good bye!")


