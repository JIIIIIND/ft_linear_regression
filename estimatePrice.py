import sys

def loadingTheta():
    theta0 = 0
    theta1 = 0
    try:
        with open("init.txt", "r") as f:
            line = f.readline()
            sep = line.index(' ')
            theta0 = float(line[0:sep])
            theta1 = float(line[(sep + 1):])
    except:
        theta0 = 0
        theta1 = 0
    return (theta0, theta1)

def estimatePrice(mileage):
    (theta0, theta1) = loadingTheta()
    print(theta0 + (mileage * theta1))

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("write mileage")
    else:
        value = float(sys.argv[1])
        estimatePrice(value)
