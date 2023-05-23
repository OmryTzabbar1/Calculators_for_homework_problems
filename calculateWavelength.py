import math

def calculateChangeOfElectronEnergy(Final, Initial):
    Energy = (-2.18 * math.pow(10, -18)) * ((1 / math.pow(Final, 2)) - (1 / math.pow(Initial, 2)))
    print(Energy)
    return Energy

Final = int(input("\nEnter final energy level: "))
Initial = int(input("\nEnter initial energy level: "))

ChangeOfElectronEnergy = calculateChangeOfElectronEnergy(Final, Initial)

def calculateWavelength(Energy):
    if Energy < 0:
        Energy = -Energy
    Wavelength = (((6.626 * math.pow(10,-34)) * (3.00 * math.pow(10,8))) / (Energy))
    print(Wavelength)
    return Wavelength

Wavelength = calculateWavelength(ChangeOfElectronEnergy)
WavelengthNM = Wavelength * math.pow(10,9)