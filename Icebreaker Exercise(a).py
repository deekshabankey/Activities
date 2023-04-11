"""
Problem -I 
The wavelength of visible light ranges from 380 to 750 nanometers (nm). While the
spectrum is continuous, it is often divided into 6 colors as shown below:

Violet 380 to less than 450
Blue 450 to less than 495
Green 495 to less than 570
Yellow 570 to less than 590
Orange 590 to less than 620
Red 620 to 750

Write a program that reads a wavelength from the user and reports its color. Display
an appropriate error message if the wavelength entered by the user is outside of the
visible spectrum.
"""

n=int(input())
if(n>=380 and n<450):
    print('Violet')
elif(n>=450 and n<495):
    print('Blue')
elif(n>=495 and n<570):
    print('Green')
elif(n>=570 and n<590):
    print('Yellow')
elif(n>=590 and n<620):
    print('Orange')
elif(n>=620 and n<=750):
    print('Red')
else:
    print('Invalid Input')
