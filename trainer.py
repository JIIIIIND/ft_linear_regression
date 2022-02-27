import estimatePrice
import sys
from typing import List

learningRate = 0.5

def loadingData(path: str):
    result = []
    try:
        with open(path) as f:
            lines = f.readlines()
            for line in lines:
                line = line.replace("\n", "")
                values = line.split(',')
                if (len(values) == 2 and values[0].isnumeric() and values[1].isnumeric()):
                    result.append((int(values[0]), int(values[1])))
    except Exception as e:
        print("file read error", e)
        return []
    return result

def normalization(lst):
    x = []
    y = []
    for item in lst:
        x.append(item[0])
        y.append(item[1])
    xMin = min(x)
    xMax = max(x)
    yMin = min(y)
    yMax = max(y)
    result = []
    for item in lst:
        normalX = (item[0] - xMin) / (xMax - xMin)
        normalY = (item[1] - yMin) / (yMax - yMin)
        result.append((normalX, normalY))
    return (xMin, xMax, yMin, yMax, result)

def estimate(mileage, bias, weight):
    return weight * mileage + bias

def calcBias(lst, bias, weight):
    global learningRate
    sum = 0.0
    for i in range(len(lst)):
        sum += estimate(lst[i][0], bias, weight) - lst[i][1]
    sum = sum / len(lst) * learningRate
    return sum

def calcWeight(lst, bias, weight):
    sum = 0.0
    global learningRate
    for i in range(len(lst)):
        sum += (estimate(lst[i][0], bias, weight) - lst[i][1]) * lst[i][0]
    sum = sum / len(lst) * learningRate
    return sum

def writeValue(values):
    try:
        with open("init.txt", "w") as f:
            line = f"{values[0]}" + " " + f"{values[1]}" + " " + f"{values[2]}" + " " + f"{values[3]}" + " " + f"{values[4]}" + " " + f"{values[5]}"
            f.write(line)
    except:
        print("write error")

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("write csv data path")
    else:
        data = loadingData(sys.argv[1])
        normalData = normalization(data)
        (theta0, theta1, xMin, xMax, yMin, yMax) = estimatePrice.loadingTheta()
        xMin = normalData[0]
        xMax = normalData[1]
        yMin = normalData[2]
        yMax = normalData[3]
        for i in range(10000):
            tmpTheta0 = calcBias(normalData[4], theta0, theta1)
            tmpTheta1 = calcWeight(normalData[4], theta0, theta1)
            theta0 = theta0 - tmpTheta0
            theta1 = theta1 - tmpTheta1
        writeValue((theta0, theta1, xMin, xMax, yMin, yMax))
