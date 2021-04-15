Height=float(input("Enter your height in centimeters(cm): "))   #152.5+22.86 = 175.26(5 feet 9 inch)
Weight=float(input("Enter your Weight in Kilogram(Kg): "))      #62
Height = Height/100
BMI=Weight/(Height*Height)
print("Your Body Mass Index(BMI) is ",BMI)
if(BMI>0):
	if(BMI<=16):
		print("You are severely underweight")
	elif(BMI<=18.5):
		print("You are underweight")
	elif(BMI<=25):
		print("You are Healthy")
	elif(BMI<=30):
		print("You are overweight")
	else: print("You are severely overweight")
else:   print("Enter Valid Details")