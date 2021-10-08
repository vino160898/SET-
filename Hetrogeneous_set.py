#getting string
s={'vinoth','kumar',True,2,3,4,5.6}
for i in s:
	#if isinsitance(i,str):
	if type(i) is str:
		print(i)
#getting Articals count:
st='an apple a day keeps the doctor away, this is a famous proverb. '
st2={'a','an','the'}
st1=set(st.split())
print(len(st2 & st1))
