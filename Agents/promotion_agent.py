import pandas as pd


class PromotionAgent:
    def __init__(self):
        self.promotions = pd.read_csv("data/promotions.csv")

    def check_promotion(self, brand, category, price):
        for _, promo in self.promotions.iterrows():

            brand_match = str(promo["brand"]).lower() == brand.lower()
            category_match = str(promo["category"]).lower() == category.lower()
            price_match = price >= float(promo["min_purchase"])

            if brand_match and category_match and price_match:

                discount_percent = float(promo["discount_percent"])

                discount_amount = price * discount_percent / 100
                final_price = price - discount_amount

                return {
                    "promotion_available": True,
                    "discount_percent": discount_percent,
                    "discount_amount": round(discount_amount, 2),
                    "final_price": round(final_price, 2),
                    "description": promo["description"]
                }

        return {
            "promotion_available": False,
            "discount_percent": 0,
            "discount_amount": 0,
            "final_price": price,
            "description": "No promotion available"
        }