import pandas as pd


class RecommendationAgent:
    def __init__(self):
        self.products = pd.read_csv("data/products.csv")

    def recommend_alternatives(
        self,
        category,
        size=None,
        max_price=None,
        exclude_product=None
    ):
        products = self.products.copy()

        # Same category
        products = products[
            products["category"].str.lower() == category.lower()
        ]

        # Only products in stock
        products = products[
            products["stock"] > 0
        ]

        # Match size if provided
        if size is not None:
            products = products[
                products["size"].astype(str).str.lower()
                == str(size).lower()
            ]

        # Stay within customer's budget
        if max_price is not None:
            products = products[
                products["price"] <= max_price
            ]

        # Don't recommend the original product
        if exclude_product:
            products = products[
                products["product_name"].str.lower()
                != exclude_product.lower()
            ]

        # Recommend highest-rated products first
        products = products.sort_values(
            by="rating",
            ascending=False
        )

        return products.head(3)