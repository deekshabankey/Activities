"""
Earthquake:  Calculate temperature that a person feels because of the wind (Python3)
"""

a=float(input())
if a<=0:
    print("No Earthquake")
elif a>0 and a<2:
    print("Micro Earthquake")
elif a>=2 and a<3:
    print("Very Mionr Earthquake")
elif a>=3 and a<4:
    print("Minor Earthquake")
elif a>=4 and a<5:
    print("Light Earthquake")
elif a>=5 and a<6:
    print("Moderate Earthquake")
elif a>=6 and a<7:
    print("Strong Earthquake")
elif a>=7 and a<8:
    print("Major Earthquake")
else:
    print("Great Earthquake")
