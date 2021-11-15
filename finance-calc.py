import numpy as np
from inspect import signature

def lumpsum(principal=25000, rate=.48, time=1):
    invest = principal
    returnamt = 0

    for year in range(int(time)):
        ret = principal * rate
        principal += ret
        returnamt += ret
    print(f"return amount: {returnamt} \n total value:{invest+returnamt}")
    return int(principal), int(returnamt)

def main():

    sig = signature(lumpsum)
    params = len(sig.parameters)
    arglist = []
    for name in sig.parameters:
        try:
            inp = float(input(f"give value for {name}:"))
        except ValueError:
            inp = sig.parameters[name].default
        arglist.append(inp)
    print(arglist)
    ls = lumpsum(*arglist)

main()
