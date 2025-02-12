import sys

fs = ["football", "basketball", "baseball", "tennis", "volleyball"]

print("These are your favourite sports: " )
print(fs)

while True:
    print("These are your favourite sports: " + str(fs))
    y = input("Would you like to change anything? ").lower()

    if y == "yes":
        print("What would you like to change?")
        wt = input("A = Would you like to add something. \nB = Would you like to delete something. \nC = Would you like to change something in the list. \nD = Would you like to sort the list A-Z\nNo = Show end product\nEnd = End sequence\n")
    
        if wt == "A":
            ns = input("What sport would you like to add? ")
            fs.append(ns)
        elif wt == "B":
            sd = input("What sport would you like to delete? ")
            if sd in fs:
                fs.remove(sd)
            else:
                print(sd + "is not in the list.")
        elif wt == "C":
            cs = input("Which sport would you like to change? ")
            if cs in fs:
                csi = input("What would you like to replace it with? ")
                fs[fs.index(cs)] = csi
            else:
                print(cs + "is not in the list.")
        elif wt == "D":
            fs.sort()
            print("The list has been sorted A-Z.")
            print(fs)

        elif wt == "No":
             sys.exit()
            
    elif y == "no":
        sys.exit()
            
    


    else:
        print("Please choose A, B, C, or D. ")