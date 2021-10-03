speed = int(input("Enter the speed of the wind"))
if speed < 137 and speed >= 0:
    print("Minor")
elif speed >= 137 and speed < 177:
    print("Moderate")
elif speed >= 177 and speed < 217:
    print("Considerate")
elif speed >= 217 and speed < 266:
    print("Severe")
elif speed >= 266 and speed < 322:
    print("Devastating")
elif speed >= 322:
    print("Incredible")
else:
    print("Error")