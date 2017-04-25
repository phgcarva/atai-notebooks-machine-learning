import time

def fib(n):
	f = [x for x in range(n)]
	f[0] = 1
	if n==1:
		return f
	f[1] = 1
	if n==2:
		return f
	for i in range(2,n):
		f[i] = f[i-1] + f[i-2]
	return f

start_time = time.time()
fib(1)
print("f(1): {}".format(time.time() - start_time))

start_time = time.time()
fib(1000000)
print("f(10000): {}".format(time.time() - start_time))