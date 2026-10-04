from Agents.promotion_agent import PromotionAgent


agent = PromotionAgent()

result = agent.check_promotion(
    brand="Nike",
    category="Running Shoes",
    price=4499
)

print("\nPromotion Result:\n")

print("Promotion Available:", result["promotion_available"])
print("Discount:", result["discount_percent"], "%")
print("Discount Amount: Rs.", result["discount_amount"])
print("Original Price: Rs.", 4499)
print("Final Price: Rs.", result["final_price"])
print("Offer:", result["description"])