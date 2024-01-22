print("Program to convert Temperature from Fahrenheit to Celsius")
print("========================================================")
print("1:Fahrenheit To cesius ")
print("2:celsius to Farenhiet")
choice = int(input("Select the option (1-2): "))

temp1 = float(input("Enter temperature : "))


temp2 = (temp1 - 32) * 5/9
temp3 = (temp1 * 9/5) + 32




if choice == 1:
    
    print("The temperature in Celsius is", temp2)

elif choice == 2:
    print("The temprature in Farenheit is",temp3)
    
    





