
def main():
    x1=int(input("x1:")) ; y1=int(input("y1:"))
    x2=int(input("x2:")) ; y2=int(input("y2:"))
    x3=int(input("x3:")) ; y3=int(input("y3:"))

    points = [
    (x1,y1), 
    (x2,y2),
    (x3,y3)
    ]
    
    distances = []
    
    for i in range(len(points)):   
        for j in range(i+1,len(points)):
            x1,y1 = points[i]
            x2,y2 = points[j]
            distance = euclideanDistance(points[i],points[j])
            distances.append(distance)
            
            print(f"distance between {points[i]} and {points[j]} is {distance:.2f}")
        
    print("Minimum distance:",minDistance(distances))    
        




def euclideanDistance(point1,point2):
    x1, y1 = point1
    x2, y2 = point2
    return  ((x2-x1)**2 + (y2-y1)**2)**0.5   #d = √(x₂-x₁)²+(y₂-y₁)²

def minDistance(dist):
    min_value = float('inf')
    
    for d in dist:
       if d < min_value:
           min_value = d  # Daha küçük bir değer bulunduğunda güncelle
    
    return min_value
    
    
    
    
  
if __name__ == "__main__":
    main()   