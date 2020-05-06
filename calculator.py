import logging

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
    c = Claculator()

    add = c.add(x,y)
    sub = c.sub(x,y)
    mul = c.mul(x,y)
    div = c.div(x,y)
    print(add)
    print(sub)
    print(mul)
    print(div)

    logging.basicConfig(filename="logFile.txt",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S', level=logging.DEBUG)
    
    logging.info("Inputs : %d and %d", x, y)
    logging.info("Summation : %d", add)
    logging.info("Difference : %d", sub)
    logging.info("Multiplication : %d", mul)
    logging.info("Division : %d", div)



