def ftc(temperature):
    celsius = 5/9 *(temperature-32)
    return celsius

def ctf(temperature):
    fahrenheit = (9/5 * temperature) + 32
    return fahrenheit

print("\n1) Fahrenheit to Celsius\n2) Celsius to Fahrenheit\n")
choice = int(input("Enter your choice:- "))
if(choice==1):
    temp_in_fahr = float(input("Enter temperature in Fahrenheit : "))
    temp_in_cel = ftc(temp_in_fahr)
    print("Temperature in Celsius is {:.2f}".format(round(temp_in_cel, 2)))
elif(choice==2):
    temp_in_cel = float(input("Enter temperature in Celsius : "))
    temp_in_fahr = ctf(temp_in_cel)
    print("Temperature in Fahrenheit is {:.2f}".format(round(temp_in_fahr, 2)))
else:
    print("Enter valid Choice\n")

