from Agents.product_query_agent import ProductQueryAgent
from Agents.inventory_agent import InventoryAgent
from Agents.promotion_agent import PromotionAgent
from Agents.recommendation_agent import RecommendationAgent
from Agents.personalization_agent import PersonalizationAgent
from Agents.escalation_agent import EscalationAgent


class OrchestratorAgent:

    def __init__(self):
        self.query_agent = ProductQueryAgent()
        self.inventory_agent = InventoryAgent()
        self.promotion_agent = PromotionAgent()
        self.recommendation_agent = RecommendationAgent()
        self.personalization_agent = PersonalizationAgent()
        self.escalation_agent = EscalationAgent()

    def process_request(self, user_query):

        # STEP 1: Understand the customer's request
        query_data = self.query_agent.understand_query(user_query)

        brand = query_data.get("brand")
        category = query_data.get("category")
        color = query_data.get("color")
        size = query_data.get("size")
        max_price = query_data.get("max_price")

        # STEP 2: Search inventory
        products = self.inventory_agent.search_products(
            brand=brand,
            category=category,
            color=color,
            size=size,
            max_price=max_price
        )

        result = {
            "query_data": query_data,
            "product_found": False,
            "product": None,
            "promotion": None,
            "alternatives": None,
            "addons": None,
            "escalation": None
        }

        # STEP 3: Product is available
        if not products.empty:

            product = products.iloc[0]

            result["product_found"] = True

            result["product"] = {
                "product_name": product["product_name"],
                "brand": product["brand"],
                "category": product["category"],
                "color": product["color"],
                "size": product["size"],
                "price": float(product["price"]),
                "stock": int(product["stock"]),
                "rating": float(product["rating"])
            }

            # STEP 4: Check promotion
            promotion = self.promotion_agent.check_promotion(
                brand=product["brand"],
                category=product["category"],
                price=float(product["price"])
            )

            result["promotion"] = promotion

            # STEP 5: Recommend add-ons
            addons = self.personalization_agent.recommend_addons(
                category=product["category"]
            )

            result["addons"] = addons

        # STEP 6: Exact product not available
        else:

            if category:

                alternatives = self.recommendation_agent.recommend_alternatives(
                    category=category,
                    size=size,
                    max_price=max_price
                )

                result["alternatives"] = alternatives

            # Escalate only when no alternatives are found
            if (
                result["alternatives"] is None
                or result["alternatives"].empty
            ):

                escalation = self.escalation_agent.create_escalation(
                    customer_request=user_query,
                    reason="Requested product is unavailable",
                    attempted_solution="No suitable alternatives were found"
                )

                result["escalation"] = escalation

        return result