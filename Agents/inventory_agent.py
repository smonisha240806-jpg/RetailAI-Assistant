import pandas as pd


class InventoryAgent:

    def __init__(self, data_path="data/products.csv"):
        self.products = pd.read_csv(data_path)

    def search_products(
        self,
        brand=None,
        category=None,
        color=None,
        size=None,
        max_price=None
    ):

        results = self.products.copy()

        if brand:
            results = results[
                results["brand"].str.lower() == brand.lower()
            ]

        if category:
            results = results[
                results["category"].str.lower() == category.lower()
            ]

        if color:
            results = results[
                results["color"].str.lower() == color.lower()
            ]

        if size:
            results = results[
                results["size"].astype(str).str.lower()
                == str(size).lower()
            ]

        if max_price:
            results = results[
                results["price"] <= max_price
            ]

        # Only show products currently available
        results = results[
            results["stock"] > 0
        ]

        return results