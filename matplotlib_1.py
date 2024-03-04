import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,16,2)
y = [x*2 for x in x]
def plot1(x,y) :
    plt.plot(x,y,color="green", linestyle = "--" ,marker="x",markersize = 12,linewidth=2)
    plt.xlabel("time (s)",fontsize= 20),plt.title("Velocity-Time Graph",fontsize = 30,color="blue"), plt.ylabel("velocity (m/s)",fontsize= 20)
    plt.grid() # imaginary lines inside the graph
    #plt.legend(loc = 'upper right')
    plt.axhline(color = "red",zorder = -1)
    plt.axvline(color = "red",zorder = -1)
    plt.show()
    plt.savefig("graph.pdf") # to save the graph figure in the directory
plot1(x,y)