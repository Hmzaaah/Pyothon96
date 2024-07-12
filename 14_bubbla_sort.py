#كود ترتيب القيم او االيانات العشوائية
grades =[10 , 21 , 6 ,15 ,20 ,5]#>[5 ,6 ,10,15 ,20]

print(grades)
#bubble sort algorthm
#1)Length for array

length =len (grades)

#2)loop on elemwnt in array
for index in range(0 ,length-1):
  for compare in range(0 ,length - index -1):
    first =grades[compare]
    second =grades[compare+ 1]
    if first >second:
        grades[compare] =second
        grades[compare+ 1] =first


print(grades)
print("Highest Grade: " + str(grades[-1]))
print("Loweset Grade: " + str(grades[0]))