#import math
#def point(x1,y1,x2,y2):
#distance=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
 #   return(distance)
#p =point(2,3,4,5)
#print(p)
class point():
    x=0
    y=0
p1=point()
p2=point()
p1.x=1
p1.y=2
p2.x=6
p2.y=3
import math
def distance(p1,p2):
    distance=(math.sqrt(((p1.x-p2.x)**2)+((p1.y-p2.y)**2)))
    return (distance)
print(distance(p1,p2))
# p =point(2,3,4,5)
# print(p)

