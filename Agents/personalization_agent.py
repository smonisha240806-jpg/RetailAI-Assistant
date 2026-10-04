import pandas as pd


class PersonalizationAgent:
    def __init__(self):
        self.products = pd.read_csv("data/products.csv")

    def recommend_addons(self, category):
        category = category.lower()

        # Decide suitable add-on categories
        if category == "running shoes":
            addon_categories = ["Socks", "Accessories"]

        elif category == "casual shoes":
            addon_categories = ["Socks"]

        elif category == "t-shirt":
            addon_categories = ["Shorts", "Accessories"]

        else:
            addon_categories = ["Accessories"]

        # Find matching add-ons
        recommendations = self.products[
            self.products["category"].isin(addon_categories)
        ]

        # Only recommend available products
        recommendations = recommendations[
            recommendations["stock"] > 0
        ]

        # Highest-rated products first
        recommendations = recommendations.sort_values(
            by="rating",
            ascending=False
        )

        return recommendations.head(3)