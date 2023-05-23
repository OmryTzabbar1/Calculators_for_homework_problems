import math

def calculateChangeOfElectronEnergy(Final, Initial):
    Energy = (-2.18 * math.pow(10, -18)) * ((1 / math.pow(Final, 2)) - (1 / math.pow(Initial, 2)))
    print(f"{Energy:.2e} J")
    return Energy

def calculateWavelength(Energy):
    Wavelength = ((6.626 * math.pow(10, -34)) * (3.00 * math.pow(10, 8))) / float(Energy)
    WavelengthNM = Wavelength / math.pow(10,-9)
    print(f"{WavelengthNM:.2f} nm")
    return WavelengthNM

while True:
    initial = int(input())
    final = int(input())
    Energy = calculateChangeOfElectronEnergy(final, initial)

    calculateWavelength(Energy)



