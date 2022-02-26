def estimatePrice(mileage):
    theta0 = 0
    theta1 = 0
    try:
        with open("init.txt", "r") as f:
            line = f.readline()
            sep = line.index(' ')
            theta0 = float(line[0:(sep - 1)])
            theta1 = float(line[(sep + 1):])
    except:
        theta0 = 0
        theta1 = 0
    print(theta0 + (mileage * theta1))

value = input()
estimatePrice(value)

