temperatures=[10,-20,-289,100]
def c_to_f(c):
    if c > -273.15:
        f=c*9/5+32
        return f
    else:
        return "Temperature cannot be less than -273.15"

for cf in temperatures:
    print(c_to_f(cf))
