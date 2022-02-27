import sys

def loadingTheta():
    theta0 = 0
    theta1 = 0
    xMin = 0
    xMax = 0
    yMin = 0
    yMax = 0
    try:
        with open("init.txt", "r") as f:
            line = f.readline()
            values = line.split(" ")
            theta0 = float(values[0])
            theta1 = float(values[1])
            xMin = int(values[2])
            xMax = int(values[3])
            yMin = int(values[4])
            yMax = int(values[5])
    except Exception as e:
        pass
    return (theta0, theta1, xMin, xMax, yMin, yMax)

def estimatePrice(mileage):
    (theta0, theta1, xMin, xMax, yMin, yMax) = loadingTheta()
    if xMin == 0 and xMax == 0:
        return 0
    normalValue = theta0 + theta1 * ((mileage - xMin) / (xMax - xMin))
    return (normalValue * (yMax - yMin) + yMin)

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("write mileage")
    else:
        value = int(sys.argv[1])
        print(estimatePrice(value))
