import numpy as np
import matplotlib.pyplot as plt
Array = np.ones([5,5])
zeros = np.zeros((3,3))
zeros[1,1] = 11
Array[1:-1,1:-1] = zeros
# x = [1,2,3,4,5,6]
# y = [10,2,20,3,30,4]
Array[1:-1,1:-1] = zeros
pi = np.pi
# x = np.arange(-5*pi,5*pi,0.001)
# y = np.sin(x)
x = np.arange(-6*1/2,6*1/2,1)
y = np.sin(x)
plt.plot(
    x ,y,
    color = "red",
    linestyle = "solid",
    marker = '.'
)
plt.legend()
plt.xlabel = " velocity(m/s2)"
plt.ylabel = "time(s)"
plt.title = " Velocity Time Graph "
plt.grid()
plt.show()
