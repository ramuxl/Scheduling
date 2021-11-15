# Recursive function that evaluates the stack
def evaluateStackR( s , resourceConstraint ):
  #TotalOperationsR = [0,0,0,0,0]
  #CounterOperationsR = [0,0,0,0,0]
  #CentinelOperationsR = [1,1,1,1,1]
  print ("--",resourceConstraint)
  print ("***",CounterOperationsR)
  print ("=====",CentinelOperationsR)
  global NumUnitR
  
  global TotalAdditions,TotalSubtrations,TotalMultiplications,Totaldivisions,CounterOperationsR,CentinelOperationsR
  #Result.clear()
  op = s.pop()
  if op == "NOT":
	  return "NOT"
  if op in "+-*/^":
	
    if op == "+":
      if resourceConstraint[0] >= CounterOperationsR[0]:
          Step = CentinelOperationsR[0]
          CounterOperationsR[0] = CounterOperationsR[0] + 1
      elif  resourceConstraint[0] == 0:
          print ("NOT +")
          return "It's imposible"
      else:
          CounterOperationsR[0] = 1
          CentinelOperationsR[0] = CentinelOperationsR[0] + 1
          Step = CentinelOperationsR[0]
    elif op == "-":
      if resourceConstraint[1] > CounterOperationsR[1] and CentinelOperationsR[1] == 1:
          Step = CentinelOperationsR[1]
          CounterOperationsR[1] = CounterOperationsR[1] + 1
      elif resourceConstraint[1]-1 > CounterOperationsR[1] and CentinelOperationsR[1] > 1:
          Step = CentinelOperationsR[1]
          CounterOperationsR[1] = CounterOperationsR[1] + 1
      elif  resourceConstraint[1] == 0:
          print ("It's imposible")
          return "It's imposible"
      else:
          CounterOperationsR[1] = 1
          CentinelOperationsR[1] = CentinelOperationsR[1] + 1
          Step = CentinelOperationsR[1]
    elif op == "*":
      if resourceConstraint[2] > CounterOperationsR[2] and CentinelOperationsR[2] == 1:
          Step = CentinelOperationsR[2]
          CounterOperationsR[2] = CounterOperationsR[2] + 1
      elif resourceConstraint[2]-1 > CounterOperationsR[2] and CentinelOperationsR[2] > 1:
          Step = CentinelOperationsR[2]
          CounterOperationsR[2] = CounterOperationsR[2] + 1
      elif  resourceConstraint[2] == 0:
          print ("NOT *")
          return "It's imposible"
      else:
          CounterOperationsR[2] = 1
          CentinelOperationsR[2] = CentinelOperationsR[2] + 1
          Step = CentinelOperationsR[2]
    elif op == "/":
      if resourceConstraint[3] > CounterOperationsR[3] and CentinelOperationsR[3] == 1:
          Step = CentinelOperationsR[3]
          CounterOperationsR[3] = CounterOperationsR[3] + 1
      elif resourceConstraint[3]-1 > CounterOperationsR[3] and CentinelOperationsR[3] > 1:
          Step = CentinelOperationsR[3]
          CounterOperationsR[3] = CounterOperationsR[3] + 1
      elif  resourceConstraint[3] == 0:
          print ("NOT /")
          return "It's imposible"
      else:
          CounterOperationsR[3] = 1
          CentinelOperationsR[3] = CentinelOperationsR[3] + 1
          Step = CentinelOperationsR[3]
	
	
	
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
            if resourceConstraint[0] >= CounterOperationsR[0]:
                Step = 1
                CounterOperationsR[0] = CounterOperationsR[0] + 1
            elif  resourceConstraint[0] == 0:
                print ("NOT +")
                return "It's imposible"
            else:
                CounterOperationsR[0] = 1
                CentinelOperationsR[0] = CentinelOperationsR[0] + 1
                Step = CentinelOperationsR[0]
            		
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
