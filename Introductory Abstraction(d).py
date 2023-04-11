"""
Factor:  Calculate temperature that a person feels because of the wind (Python3)
"""
def Earthquake(a):
    if a<=0:
        return"No Earthquake"
    elif a>0 and a<2:
        return"Micro Earthquake"
    elif a>=2 and a<3:
        "Very Mionr Earthquake"
    elif a>=3 and a<4:
        return "Minor Earthquake"
    elif a>=4 and a<5:
        return "Light Earthquake"
    elif a>=5 and a<6:
        return "Moderate Earthquake"
    elif a>=6 and a<7:
        return "Strong Earthquake"
    elif a>=7 and a<8:
        return "Major Earthquake"
    else:
        return "Great Earthquake"
print(Earthquake(1))
