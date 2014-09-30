import os
def findfiles(tree):
  
  for one in tree:
    filn=os.listdir(one)
    
    for each in filn:
 
      if os.path.isdir(one+'/'+each):
        
        
        yield one+'/'+each
      else:
        print os.path.abspath(one+'/'+each)
