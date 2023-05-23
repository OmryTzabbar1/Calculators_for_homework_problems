import math

def calculateFrequency(wavelength):
    wavelength = wavelength * math.pow(10, -9)
    Frequency = ((3.00 * math.pow(10, 8)) / wavelength)
    print(f"\nThe Frequency is: {Frequency:.2e} Hz")
    return Frequency

while True:
    Wavelength = float(input("\nEnter the Wavelength: "))
    calculateFrequency(Wavelength)



