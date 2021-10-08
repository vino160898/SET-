s1={10,20,30}
s2={30,40,50}
print(s1 | s2) #-->no duplicates.
print(s1 & s2) #-->common value.
print(s1 - s2) #-->s2 is present value to removing s1.
print(s2 - s1) #-->s1 is present value to removing s2.
print(s1 ^ s2) #-->s1 and s2 is present values totaly removing.

|  -->s1.union(s2)
&  -->s1.intersection(s2)
-  -->s1.difference(s2)
^  -->s1.symmetric_difference(s2)
