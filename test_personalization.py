from Agents.personalization_agent import PersonalizationAgent


agent = PersonalizationAgent()

results = agent.recommend_addons(
    category="Running Shoes"
)

print("\nRecommended Add-ons:\n")

if results.empty:
    print("No add-ons available.")

else:
    print(
        results[
            [
                "product_name",
                "brand",
                "category",
                "price",
                "stock",
                "rating"
            ]
        ].to_string(index=False)
    )