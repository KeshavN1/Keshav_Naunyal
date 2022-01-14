km = []
miles = []
print("\nSwallow Speed Analysis: Version 1.0\n")
while True:#it loops the program
    s = input("Enter the Next Reading: ")
    if s == "": #if input is nothing it break the loop
        break
    print(" Reading saved\n")
    speed = float(s[1:])
    miles.append(speed) if s[0].lower() == "u" else km.append(speed) 
newlst = miles.copy()
miles += [i*0.621371 for i in km]
km += [i*1.60934 for i in newlst]
if len(km) != 0:
    print("Results Summary\n")
    print("{} Reading Analysed.\n".format(len(km)))
    print("Max is {:.2f} KPH and {:.2f} MPH".format(max(km), max(miles)))
    print("Min is {:.2f} KPH and {:.2f} MPH".format(min(km), min(miles)))
    print("Average is {:.2f} KPH and {:.2f} MPH".format(sum(km)/len(km), sum(miles)/len(miles)))
else:
    print("No readings entered. Nothing to do.")
