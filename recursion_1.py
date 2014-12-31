a = [1,3,5,7,9]
def sum_list(a):
	if len(a)==1:
		return a[0]
	else:
		return a[0] + sum_list(a[1:])
print sum_list(a)

