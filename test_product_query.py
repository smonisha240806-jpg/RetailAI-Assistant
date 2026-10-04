from Agents.product_query_agent import ProductQueryAgent


agent = ProductQueryAgent()

query = "Customer wants black Nike running shoes size 8 under Rs. 5000"

result = agent.understand_query(query)

print("\nOriginal Customer Request:")
print(query)

print("\nAI Extracted Information:\n")

print("Brand:", result["brand"])
print("Category:", result["category"])
print("Color:", result["color"])
print("Size:", result["size"])
print("Maximum Price:", result["max_price"])