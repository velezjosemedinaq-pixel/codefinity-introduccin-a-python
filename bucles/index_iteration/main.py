prices = [29.99, 45.50, 12.75, 38.20]

for i in range(len(prices)):
    if i == 0:
           descuento = 0.10
    elif i == 1:
           descuento = 0.20
    elif i == 2:
           descuento = 0.15
    elif i == 3:
           descuento = 0.05

    prices[i] = prices[i] * (1 - descuento)
    print(f"Updated price for item {i}: ${prices[i]:.2f}")