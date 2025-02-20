import matplotlib.pyplot as plt
import numpy as np

#getting the points from the user
n=int(input("enter number of points:"))
points=[]

for i in range(n):
    x=float(input("Enter x value for point "+str(i+1)+": "))
    y=float(input("Enter y value for point "+str(i+1)+": ")) 
    points.append((x,y))#append as tuple
points=np.array(points)#convert list of tuples to a numPy array

nn=[]#the nearedt neighbour
taken=set()#points from which lines are already drawn

#find distnaces to each point from a particular a particular point and store it in dictionary
for i, point in enumerate(points):
    distances={}#Dictionary to store distances as {neighbor_point: distance}
    for j,other in enumerate(points):
        if i != j: 
            dist=np.linalg.norm(point-other)
            distances[tuple(other)]=dist#Stores in dictionary

    #Sorting dictionary by distance
    sortd=sorted(distances.items(),key=lambda x:x[1])

    #Finding the first available neighbor
    nearest=None
    for neighbour,_ in sortd:
        if neighbour not in taken:
            nearest = neighbour
            break

    nn.append(nearest)
    taken.add(tuple(point))#Marking current point as connected

#Ploting points
plt.figure(figsize=(8,8))
plt.scatter(points[:,0],points[:,1],color='red')

#plotting lines
for i in range(len(points)):
    point=points[i]
    neighbour=nn[i]
    
    if neighbour is not None:  
        plt.plot([point[0], neighbour[0]], [point[1], neighbour[1]], 'purple', lw=1)


plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("nearest neighbours without duplicates")
plt.grid()
plt.show()

 