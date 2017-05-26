import numpy as np

x = np.arange(-2.0, 6.0, 0.1)

print(sum(np.exp(x)))

print np.divide(np.exp(x), sum(np.exp(x)))
print np.sum(np.divide(np.exp(x), sum(np.exp(x))))

ones = np.ones_like(x)

print np.divide(np.exp(ones), sum(np.exp(ones)))

a = 1000000000

for i in xrange(1000000):
	a += 0.000001

a = a - 1000000000

print a