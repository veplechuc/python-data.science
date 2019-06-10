import matplotlib.pyplot as plt
import numpy as np

x= np.linspace(0,5,11)
y = x**3

#define some canvas
# fig = plt.figure()
# l = [0.1,0.1,0.5,0.5] #values should be between 0-1
# axes = fig.add_axes(l)
# axes.set_title('Titulo')
#axes.plot(x,y)
#plt.show()


#two plots
fig, axes = plt.subplots(nrows=1, ncols=2) #a way to avoid add axes method
print(fig)
print(axes) #is an array
axes[0].plot(x,y) 
axes[1].plot(y,x)
plt.show()