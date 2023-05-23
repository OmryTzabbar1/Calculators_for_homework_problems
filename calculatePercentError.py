def calculatePercentError(observed, expected):
    PercentError = ((observed - expected) / expected) * 100
    print(f"\nPercent Error: {PercentError:.2f}")
    return PercentError


while True:
    observed = float(input("\nEnter the observed value: "))
    expected = float(input("\nEnter the expected value: "))

    PercentError = calculatePercentError(observed, expected)
