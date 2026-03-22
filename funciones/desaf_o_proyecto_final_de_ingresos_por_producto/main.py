# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

# Example of expected output line (do not remove):
def calculate_revenue(prices, quantities_sold):
    revenue = []
    for i in range(len(prices)):

        revenue.append(prices[i] * quantities_sold[i])
    return revenue


def formatted_output(revenue_per_product):
    for product, amount in sorted(revenue_per_product):

        print(f"{product} has total revenue of ${amount}")


revenue = calculate_revenue(prices, quantities_sold)
revenue_per_product = list(zip(products, revenue))
formatted_output(revenue_per_product)