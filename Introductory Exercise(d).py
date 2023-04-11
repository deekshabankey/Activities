"""
Factor:  Calculate temperature that a person feels because of the wind (Python3)
"""
T_a=float(input('Input air temperature in degree celsius: '))
v=float(input('Input wind speed in km/h: '))
Temperature=13.12 + 0.6215 * T_a * (0.3965 * T_a - 11.37) * (v**0.16)
print(Temperature,"deg celsius")
