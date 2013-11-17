class Rectangle:
    def __init__(self,width=10,height=10):
        self.setStats(width,height)

    def setStats(self,width,height):
        self.width = width
        self.height = height

    def getStats(self):
        print "width:      %d" % self.width
        print "height:     %d" % self.height
        print "area:       %d" % self.area()
        print "perimeter:  %d" % self.perimeter()

    def area(self):
        return self.height*self.width

    def perimeter(self):
        return 2*(self.height+self.width)

def main():
    print "Rectangle a:"
    a = Rectangle(5, 7)
    print "area:      %d" % a.area()
    print "perimeter: %d" % a.perimeter()

    print ""
    print "Rectangle b:"
    b = Rectangle()
    b.width = 10
    b.height = 20
    b.getStats()

main()