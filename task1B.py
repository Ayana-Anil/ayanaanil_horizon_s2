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


#finding the nearest point
closest=[]
for i,point in enumerate(points):
    distances={}#Dictionary to store distances {otherpoint:distance}
    for j, otherpoint in enumerate(points):
        if i!=j:
            distf = np.linalg.norm(point - otherpoint) #obtains distance
            distances[tuple(otherpoint)] = distf #stores all distances in the dictionary

    #Find the nearest point by getting the key with the smallest value
    nearest = min(distances,key=distances.get)
    closest.append(np.array(nearest))


#ploting the points
plt.figure(figsize=(8,8))#setting the size of the figure
plt.scatter(points[:, 0],points[:,1],color='red')#gets the x and y co-ordinates from the array and plots those points

#ploting the lines to the nearest neighbour
for i in range(len(points)):# Loop through indices
    point=points[i]
    close=closest[i]  
    plt.plot([point[0],close[0]],[point[1],close[1]],'purple',lw=1)#plotting the line

#modifying the figure
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Nearest Neighbour Connections")
plt.grid()

plt.show()

