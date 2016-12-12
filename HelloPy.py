import sys



x = 0

for x in range (5):
  print ('hello world')

foo = sys.argv[1]  
if(foo == "-h" or foo == "--help"):
    print("Description here")
    exit() 
