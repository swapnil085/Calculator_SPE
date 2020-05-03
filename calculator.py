class Claculator:
    def add(self, x, y):
        return x+y
    def sub(self, x, y):
        return x-y
    def mul(self, x, y):
        return x*y
    def div(self, x, y):
        try:
            return x/float(y)
        except:
            return "Failed To Divide!"

if __name__ == "__main__":
    #x = int(input("Enter 1st Value: "))
    #y = int(input("Enter 1st Value: "))
    x = 6
    y = 9
    c= Claculator()
    print(c.add(x,y))
    print(c.sub(x,y))
    print(c.mul(x,y))
    print(c.div(x,y))
