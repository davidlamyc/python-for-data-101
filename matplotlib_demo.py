import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x ** 2

# plt.plot(x,y,'r-') # 'r-' defines the line style
# plt.xlabel('X Label')
# plt.ylabel('Y Label')
# plt.title('Title')

# plt.subplot(1,2,1) # arguments: no of rows, no of cols, plot no referenced
# plt.plot(x,y,'r')

# plt.subplot(1,2,2)
# plt.plot(y,x,'b')

# plt.show()

# clearer OOP method (creating figure objects and creating methods off them)
fig = plt.figure()

axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y)
axes.set_xlabel('X label')
axes.set_ylabel('Y label')
axes.set_xlabel('Set Title')

fig = plt.figure()

axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])

axes1.plot(x,y)
axes1.set_title('large plot')

axes2.plot(y,x)
axes2.set_title('small plot')

plt.show()
