from Agents.escalation_agent import EscalationAgent


agent = EscalationAgent()

result = agent.create_escalation(
    customer_request="Nike Revolution 7, Black, Size 9",
    reason="Requested product is out of stock",
    attempted_solution="Customer rejected alternative products"
)

print("\nEscalation Details:\n")

print("Status:", result["status"])
print("Customer Request:", result["customer_request"])
print("Reason:", result["reason"])
print("Attempted Solution:", result["attempted_solution"])
print("Message:", result["message"])