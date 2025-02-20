import matplotlib.pyplot as plt
import numpy
n=int(input("enter numbers of points that you want to plot:"))
x=[]
y=[]
print("enter the points")
for i in range(n):
    a=input("x:")
    x.append(a)
    b=input("y:")
    y.append(b)

plt.scatter(x,y)
plt.show()
