s={10,20,30,40,50,100}
l=[20,30,40,50,60,70,80]
s.update(l,range(3))
print(s)  #-->{0, 1, 2, 100, 70, 40, 10, 80, 50, 20, 60, 30}
s.add(75)
print(s) #-->{0, 1, 2, 100, 70, 40, 10, 75, 80, 50, 20, 60, 30}
s.update('Hi')
print(s) #-->{0, 1, 2, 100, 70, 40, 10, 75, 'H', 80, 50, 20, 'i', 60, 30}

#s.update(123)
#print(s) #-->TypeError: 'int' object is not iterable

