def linearSearch(array ,query):
 for index in range(0 , len (array)):
    if array [index] == query:
      return index
    return -1

grades =[3 , 12 ,14 ,15]
search =50
result = linearSearch(grades , search)
if result == -1:
  print("Not found")
else:
  print("found")
