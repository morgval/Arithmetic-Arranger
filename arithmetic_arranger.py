def arithmetic_arranger(problems):
  if len(problems) > 5:
    raise Exception("ERROR: Too many problems.")

  #Loop through list of problems
  i=0
  while i < len(problems):
    #search for the addition symbol
    operandLoc = problems[i].find("+")
    if operandLoc > 0:
      operand = "+"
    #if addition symbol is not found, search for subtraction symbol
    if operandLoc == -1:
      operandLoc = problems[i].find("-")
      operand = "-"
      #if subtraction symbol is not found either, raise exception
      if operandLoc == -1:
        raise Exception("ERROR: Operation must be + or -.")

    #remove white space to isolate numbers
    numberOne = problems[i][:operand].strip()
    numberTwo = problems[i][operand+1:].strip()

    #find length of numbers
    lengthOne = len(numberOne)
    lengthTwo = len(numberTwo)

    #there's definitely a better way to do this
    #find which number is longer in order to format vertically with spaces
    if lengthOne > lengthTwo:
      numberOne = "  " + numberOne
      numberTwo = operand + (" " * lengthOne) + numberTwo
      if len(numberOne) == len(numberTwo):
        dashes = "-" * len(numberTwo)
      else:
        raise Exception("Format Error: " + problems[i])
        #will remove after testing
        
    if lengthTwo > lengthOne: 
      numberTwo = operand + " " + numberTwo
      numberOne = 
      if len(numberOne) == len(numberTwo):
        dashes = "-" * len(numberTwo)
      else:
        raise Exception("Format Error: " + problems[i])
        #will remove after testing
        
    if lengthOne == lengthTwo:
      numberOne = "  " + numberOne
      numberTwo = operand + " " + numberTwo
      if len(numberOne) == len(numberTwo):
        dashes = "-" * len(numberTwo)
      else:
        raise Exception("Format Error: " + problems[i])
        #will remove after testing
         
    
    i++

    return arranged_problems
