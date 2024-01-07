def sum(self):
	return self.max + self.min
P = type("Point", (), {'max': 100, 'min': 5, 'sum': sum})
a = P()
print(a.sum())
