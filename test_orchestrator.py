from Agents.orchestrator_agent import OrchestratorAgent


agent = OrchestratorAgent()

query = "Customer wants black Nike running shoes size 9 under Rs. 5000"

result = agent.process_request(query)


print("\n========== RETAILAI RESULT ==========\n")

print("Customer Request:")
print(query)

print("\nAI Understood:")
print(result["query_data"])


if result["product_found"]:

    print("\nPRODUCT FOUND:")

    product = result["product"]

    print("Product:", product["product_name"])
    print("Brand:", product["brand"])
    print("Color:", product["color"])
    print("Size:", product["size"])
    print("Price: Rs.", product["price"])
    print("Stock:", product["stock"])
    print("Rating:", product["rating"])

    print("\nPROMOTION:")

    promotion = result["promotion"]

    print("Offer:", promotion["description"])
    print("Final Price: Rs.", promotion["final_price"])

    print("\nRECOMMENDED ADD-ONS:")

    addons = result["addons"]

    if addons is not None and not addons.empty:

        print(
            addons[
                [
                    "product_name",
                    "category",
                    "price"
                ]
            ].to_string(index=False)
        )

    else:
        print("No add-ons available.")


else:

    print("\nExact product not available.")

    alternatives = result["alternatives"]

    if alternatives is not None and not alternatives.empty:

        print("\nALTERNATIVES:")

        print(
            alternatives[
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

    if result["escalation"]:

        print("\nESCALATION:")

        print(result["escalation"]["message"])