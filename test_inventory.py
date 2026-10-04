from Agents.inventory_agent import InventoryAgent

agent = InventoryAgent()

results = agent.search_products(
    brand="Nike",
    category="Running Shoes",
    color="Black",
    size="8",
    max_price=5000
)

print("\nMatching Products:\n")

if results.empty:
    print("No matching products are currently available.")
else:
    print(
        results[
            [
                "product_name",
                "brand",
                "color",
                "size",
                "price",
                "stock"
            ]
        ].to_string(index=False)
    )