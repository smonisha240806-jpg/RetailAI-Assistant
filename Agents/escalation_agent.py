class EscalationAgent:

    def create_escalation(
        self,
        customer_request,
        reason,
        attempted_solution=None
    ):

        escalation = {
            "status": "Escalation Required",
            "customer_request": customer_request,
            "reason": reason,
            "attempted_solution": attempted_solution,
            "message": (
                "The customer request could not be resolved automatically. "
                "Please contact the store supervisor for further assistance."
            )
        }

        return escalation
