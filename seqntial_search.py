def sequential_search(search_list,item):
	pos = 0
	found = False
	while pos < len(search_list) and not found:
		if search_list[pos] == item:
			found = True
		else:
			pos = pos + 1
	return found
print sequential_search([11,22,3,44,5,66],3)
print sequential_search([11,22,3,44,5,66],77)
