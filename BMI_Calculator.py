weight=float(input("enter your weight in Kg :"))
height = float(input("enter the height in meters:"))
bmi=weight/(height * height)
print("Your BMI is: ",{round(bmi,2)})
if(0>bmi<=16):
    print("severe Underweight")
elif(bmi<=18.5):
    print("Underweight")
elif(bmi<=25):
      print("healthy")
elif(bmi<=30):
      print("Overweight")
elif(bmi>30):
    print("Severe Obesity")
else:
    print("enter valid details")
      
    
