import csv


with open ('file.csv') as file:
	text = file.readlines()
	# print (text)
	for i in range(len(text)):
		text[i] = text[i].strip() #delete space
	for i in text: print (i)
	st = text.pop(0)
	st = text.pop(0)
	# for st in text: print (st)


def form_sum(st):
	ls_st = st.split(';')
	m_sum = int(ls_st[2])
	f_sum = int(ls_st[3])
	i_sum = int(ls_st[4])
	a_sum = m_sum+f_sum+i_sum
	return a_sum, m_sum, f_sum, i_sum

a_sum1, m_sum1, f_sum1, i_sum1 = form_sum(text[1])
print (a_sum1, m_sum1, f_sum1, i_sum1)

