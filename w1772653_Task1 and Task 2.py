print("Progression program based on pass, defer and fail")

list1 = [0,20,40,60,80,100,120]

while True:
      
    try:
        
      while True:       
        Pass=int(input("Please enter your credits at a pass: "))
        if Pass in list1:
          break
        else:
          print("Out of range")

      while True:
        Defer=int(input("Please enter your credits at a defer: "))
        if Defer in list1:
          break
        else:
          print("Out of range")
      while True:
        Fail=int(input("Please enter your credits at a fail: "))
        if Fail in list1:
          break
        else:
          print("out of range")
    
      if (Pass+ Defer + Fail != 120):
        print("Total Incorrect")
      else:
        break
    except:
        print("only enter integers, repeat input")



if (Pass == 120 and Defer == 0 and Fail == 0):
    print("Progress")
    
elif (Pass==100 and Defer <= 20 and Fail <=20):
    print("Progress(Module Trailer)")


elif (Pass <=80 and Defer <=80 and Fail <= 60):
    print("Do not progress - module retriever")

elif (Pass==40 and Defer == 0 and Fail == 80):
    print("Exclude")

elif (Pass==20 and Defer <=100 and Fail <= 60):
  print("Do not progress - module retriever")

elif (Pass==20 and Defer <=20 and Fail <= 100):
  print("Exclude")

elif (Pass==0 and Defer <=120 and Fail <= 60):
    print("Do not progress - module retriever")

elif (Pass==0 and Defer <=40 and Fail <=120):
    print("Exclude")
    

  
