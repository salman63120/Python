print("Staff Version with Histogram")

list1 =[0,20,40,60,80,100,120]

#here i am assigning 4 variables for the histogram.

count_Progress=0
count_Trailer=0
count_Retriever=0
count_Exclude=0
total5=count_Progress+count_Trailer+count_Retriever+count_Exclude


while True:

  while True:

    try:
      while True:
        Pass=int(input("Please enter your credits at a pass: "))
        if Pass in list1:
          break
        else:
          print("out of range")

      while True:
        Defer=int(input("Please enter your credits at a defer: "))
        if Defer in list1:
          break
        else:
          print("out of range")

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




#if statement for pass if it is 120 then it should progress the student.
  if (Pass == 120  and Defer == 0 and Fail == 0):  
    print("Progress")
    count_Progress+=1
 
#elif statement - alternative to if statement. Defer and Fail should equal to 20.
  elif (Pass==100 and Defer <= 20 and Fail <= 20):    
    print("Progress(module trailer)")
    count_Trailer+=1
    
  elif (Pass <=80 and Defer <=80 and Fail <= 60):     
    print("Do not progress - module retriever")
    count_Retriever+=1

  elif (Pass==40 and Defer== 0 and Fail == 80):
    print("Exclude")
    count_Exclude+=1

  elif (Pass==20 and Defer <=100 and Fail <= 60):
    print("Do not progress - module retriever")
    count_Retriever+=1

  elif (Pass==20 and Defer <=20 and Fail <= 100):
    print("Exclude")
    count_Exclude+=1

  elif (Pass==0 and Defer <=120 and Fail <= 60):
    print("Do not progress - module retriever")
    count_Retriever+=1

  elif (Pass==0 and Defer <=40 and Fail <= 120):
    print("Exclude")
    count_Exclude+=1




  y = input("Enter 'y' for yes and 'q' to quit: ")
  if y == "q":
      break

print("------------------------------------------------------------")
print("Histogram")

print("Progress",count_Progress,":", count_Progress * "*")


def histogram():
    """ Trailer1: """
    print("Trailer", count_Trailer,":", count_Trailer * "*")
histogram()

def histogram():
    """ Retriever1: """
    print("Retriever", count_Retriever,":", count_Retriever * "*")
histogram()

def histogram():
    """Exclude1: """
    print("Exclude", count_Exclude,":", count_Exclude * "*")
histogram()

total=count_Progress+count_Trailer+count_Retriever+count_Exclude
print("Total outcomes are", total)

print("------------------------------------------------------------")
