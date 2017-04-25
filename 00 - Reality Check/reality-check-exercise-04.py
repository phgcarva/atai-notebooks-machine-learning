import matplotlib.pyplot as plt

def expectation(column):
	return sum(column)/len(column)

def variance(column):
	return expectation([x**2 for x in column]) - expectation(column)**2

def find_two_columns(columns):
	variances = [(i,variance(column)) for i, column in enumerate(columns)]
	variances = sorted(variances, key=lambda x: x[1])
	return variances[-1][0], variances[-2][0]
	

if __name__ == "__main__":
	with open('reality-check-data.txt') as f:
		lines = f.readlines()

	data = [line.split("   ") for line in lines]

	columns = []
	for i in range(len(data[0])):
		column = [float(el[i]) for el in data if el[i] != ""]
		columns.append(column)

	columns.pop(0)
	first, second = find_two_columns(columns)

	x = [line[first] for line in data]
	y = [line[second] for line in data]

	plt.plot(x,y)
	plt.show()