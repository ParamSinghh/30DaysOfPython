print (3+4)
print (4-3)
print (3*4)
print (12/3)
print (4%12)
print (3**4)
print (67//5)

print ("My Name is Param")
print ("I am enjoying 30 days of python")



print(type(10))      
print(type(3.14))
print(type(1+3j))
print(type(True))
print(type([1, 2, 3]))
print(type({'name':'Param', 'age':24}))
print(type(('Raman','Manraj', 'Param')))
print(type({1, 2, 3}))
print(type("Param"))



def euclidean_distance(p1, p2): #p1 and p2 are tuples representing points (x, y), these are arguments
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5 # index 0 is x coordinate, index 1 is y coordinate

point1 = (3, 4)
point2 = (7, 1)

print(euclidean_distance(point1, point2)) # calling the function with point1 and point2 as parameters