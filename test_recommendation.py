from Agents.recommendation_agent import RecommendationAgent


agent = RecommendationAgent()

results = agent.recommend_alternatives(
    category="Running Shoes",
    size="8",
    max_price=5000,
    exclude_product="Nike Revolution 7"
)

print("\nRecommended Alternatives:\n")

if results.empty:
    print("No suitable alternatives found.")

else:
    print(
        results[
            [
                "product_name",
                "brand",
                "color",
                "size",
                "price",
                "stock",
                "rating"
            ]
        ].to_string(index=False)
    )