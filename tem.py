print("****temperature converter*****")

while True:
    g = int(input("1.convert Celsius to Kelvin, 2. convert Celsius to Fahrenheit, 3.convert Fahrenheit to Celsius ,4. convert Fahrenheit to Kelvin: "))
    if g == 1:
        a=int(input("enter the  celsius value:"))
        print( "k:",a + 273.15)
    elif g == 2:
        b=int(input("enter the  celsius value:"))  
        print("F:", (9/5)*b + 32)
    elif g ==3:
        d=int(input("enter the Fahrenheit value:"))  
        print("C:", (5/9)*(d-32))
    elif g ==4:
        e=int(input("enter the  Fahrenheit value:"))  
        print("Ke :", (5/9)*(e+459.67))
    else:
        print(" enter valid input")
