from math import sqrt
from typing import List
from matplotlib import pyplot as plt


# method of primitive vectors
def primitives(a1, a2, a3):
    array_of_points = [[0, 0, 0, 1]]
    for point in array_of_points[:]:
        array_of_points.append([point[i] + a1[i] for i in range(len(point))])
        array_of_points.append([point[i] - a1[i] for i in range(len(point))])
    for point in array_of_points[:]:
        array_of_points.append([point[i] + a2[i] for i in range(len(point))])
        array_of_points.append([point[i] - a2[i] for i in range(len(point))])
    for point in array_of_points[:]:
        array_of_points.append([point[i] + a3[i] for i in range(len(point))])
        array_of_points.append([point[i] - a3[i] for i in range(len(point))])
    return array_of_points


def bcc(a, c):
    a1 = [a, 0, 0, 0]
    a2 = [0, a, 0, 0]
    a3 = [0, 0, a, 0]
    points = primitives(a1, a2, a3)
    
    # turning from cubic into bcc
    move1 = [0, 0, 0, 0]
    move2 = [a/2, a/2, a/2, 1]
    for point in points[:]:
        points.append([point[i] + move2[i] for i in range(len(point))])
        points.append([point[i] - move2[i] for i in range(len(point))])
    
    return points

def fcc(a, c):
    a1 = [a, 0, 0, 0]
    a2 = [0, a, 0, 0]
    a3 = [0, 0, a, 0]
    points = primitives(a1, a2, a3)
    
    # turning from cubic into bcc
    move1 = [0, 0, 0, 0]
    move2 = [a/2, a/2, 0, 0]
    move3 = [0, a/2, a/2, 0]
    move4 = [a/2, 0, a/2, 0]
    
    for point in points[:]:
        points.append([point[i] + move2[i] for i in range(len(point))])
        points.append([point[i] - move2[i] for i in range(len(point))])
        
    for point in points[:]:
        points.append([point[i] + move3[i] for i in range(len(point))])
        points.append([point[i] - move3[i] for i in range(len(point))])
        
    for point in points[:]:
        points.append([point[i] + move4[i] for i in range(len(point))])
        points.append([point[i] - move4[i] for i in range(len(point))])
        
    return points


def decompress(data):
    x = []
    y = []
    z = []
    type = []
    for i in range(len(data)):
        x.append(data[i][0])
        y.append(data[i][1])
        z.append(data[i][2])
        type.append(data[i][3])
    return (x, y, z, type)

if __name__ == "__main__":
    a = 1
    c = 2
    
    # a1 = [a, 0, 0, 0]
    # a2 = [a/2, sqrt(3)*a/2, 0, 0]
    # a3 = [0, 0, c, 0]
    
    # points = primitives(a1, a2, a3)
    
    points = fcc(a, c)
    
    tup = decompress(points)
    
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.scatter3D(tup[0], tup[1], tup[2], s=[tup[3][i]**2 * 15 for i in range(len(tup[3]))])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()