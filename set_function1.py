s1={10,20,30}
s2=s1.copy()
print(id(s1))
print(id(s2))
print(s2.pop())  #-->any one number getting
s2.remove(10)   #-->Inseting value delete (not present ACCORING ERROR)
s2.dicard(123)  #-->this value (not present in set NO ERROR)
s1.clear()
print(s1)
