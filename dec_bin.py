class stack:
        def __init__(self):
                self.items = []
        def is_empty(self):
                return self.items == []
        def push(self, item):
                self.items.insert(0, item)
        def pop(self):
                return self.items.pop(0)
        def peek(self):
                return self.items[0]
        def size(self):
		return len(self.items)


def dec_to_bin(x):
	s = stack()
	dec_no = x
	while dec_no > 0:
		reminder = dec_no % 2 
		s.push(reminder)
		dec_no = dec_no // 2
	binary_string = ""
	while not s.is_empty():
		binary_string = binary_string + str(s.pop())
	return binary_string
print dec_to_bin(8)
