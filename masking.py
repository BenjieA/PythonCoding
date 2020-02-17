def maskify(cc):
   array = []
   total = 0
   for i in range(1, cc+1):
       if i%3 == 0:
           array.append(i)
           total = total + i
       elif i%5 == 0:
           array.append(i)
           total = total + i
   print(total)   
       
maskify(10)
