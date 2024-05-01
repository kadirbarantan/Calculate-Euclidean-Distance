import math

points= [(12,36),(32,69),(25,87),(12,88)]


def euclideanDistance(nokta1 , nokta2):
    x1,y1=nokta1
    x2,y2=nokta2
    mesafe = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return mesafe

distances = []

for i in range(len(points)):
    for j in range(i+1, len(points)):
        mesafe = euclideanDistance(points[i], points[j])
        distances.append(mesafe)


min_mesafe= min(distances)
print("Minimum Mesafe:", min_mesafe)

