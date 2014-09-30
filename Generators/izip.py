"""zip two lists"""
def izip(a,b):
  for each in a:
    yield each,b[0]
    b=b[1:]
