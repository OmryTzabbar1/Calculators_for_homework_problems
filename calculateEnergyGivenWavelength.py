import math

def calculateEnergy(wavelength):
    wavelength = wavelength * math.pow(10,-9)
    Energy = ((6.626 * math.pow(10, -34)) * (3.00 * math.pow(10, 8))) / (wavelength)
    print(f"\nThe Energy is: {Energy:.2e} J")
    return Energy

def calculateFrequency(wavelength):
    wavelength = wavelength * math.pow(10, -9)
    Frequency = ((3.00 * math.pow(10, 8)) / wavelength)
    print(f"The Frequency is: {Frequency:.2e} Hz")
    return Frequency

def calculateNInitial(NFinal, Energy):
    Energy = -Energy
    Energy = Energy / (-2.18 * math.pow(10, -18))
    Energy = Energy - (1 / math.pow(NFinal, 2))
    Energy = -Energy
    Energy = 1 / Energy
    NInitial = math.sqrt(Energy)
    print(f"NInitial is: {NInitial:.2f}")
    return NInitial

def calculateNFinal(NInitial, Frequency):
    Wavelength = ((3.00 * math.pow(10,8))/Frequency)
    Energy = calculateEnergy(Wavelength)
    Energy = Energy / (-2.18*math.pow(10,-18))
    Energy = Energy - (1/math.pow(NInitial,2))
    Energy = 1 / Energy
    NFinal = math.sqrt(Energy)
    print(f"NFinal: {NFinal:.2f}")


while True:

    Wavelength = float(input("\nEnter the Wavelength: "))
    #calculateFrequency(Wavelength)
    calculateEnergy(Wavelength)



