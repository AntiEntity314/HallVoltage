import math

run = 1
while run == 1:
    Decide = int(input("Enter 0 to find Hall Voltage or Enter 1 to find Hall Angle: "))
    if Decide == 0:
        def HallVolt():
            I = float(input("Enter Current flowing through the wire: "))
            powI = int(input("Enter the power of 10 for current: "))
            B = float(input("Enter magnetic field value:  "))
            powB = int(input("Enter the power of 10 for magnetic field strength: "))
            n = float(input("Enter the charge carrier density: "))
            pown = int(input("Enter power of 10 for charge carrier density: "))
            e = 1.6 * pow(10,-19)
            w = float(input("Enter the width of conductor: "))
            poww = float(input("Enter power of 10 for thickness: "))
            H = ((I*pow(10,powI))*(B*pow(10,powB)))/((n*pow(10,pown))*e*w*pow(10,poww))
            print(f"Hall Voltage = {H} Volt")
        HallVolt()
    elif Decide == 1:
        def Hallang():
            mob = float(input("Enter mobility: "))
            mobpower = float(input("Enter power of 10 for mobility: "))
            B = float(input("Enter magnetic field value:  "))
            powB = int(input("Enter the power of 10 for magnetic field strength: "))
            Hallangle = math.atan(mob*mobpower*B*powB)
            print(f"Hall angle = {Hallangle} radians")
        Hallang()
    else:
        print("Invalid User Input")
