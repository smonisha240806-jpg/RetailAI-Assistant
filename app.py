import streamlit as st

from Agents.orchestrator_agent import OrchestratorAgent


# -------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------

st.set_page_config(
    page_title="RetailAI Assistant",
    page_icon="🛍️",
    layout="wide"
)


# -------------------------------------------------
# HEADER
# -------------------------------------------------

st.title("🛍️ RetailAI Assistant")

st.subheader("Agentic AI Store Support System")

st.write(
    "AI-powered digital co-worker for store associates to "
    "check products, inventory, promotions, alternatives "
    "and personalized recommendations."
)

st.divider()


# -------------------------------------------------
# AGENTIC AI WORKFLOW
# -------------------------------------------------

with st.expander("🤖 How RetailAI Agents Work"):

    st.markdown("""
### Agentic AI Workflow

**1. 🧠 Product Query Agent**  
Uses Gemini AI to understand the employee's natural-language request
and extracts the brand, category, color, size and budget.

⬇️

**2. 🎯 Orchestrator Agent**  
Decides which specialized agents should handle the request.

⬇️

**3. 📦 Inventory Agent**  
Checks whether matching products are currently available.

⬇️

**4. 🏷️ Promotion Agent**  
Checks applicable offers and calculates the discounted price.

⬇️

**5. 💡 Recommendation Agent**  
Finds suitable alternatives when the exact requested product
is unavailable.

⬇️

**6. 🛒 Personalization Agent**  
Suggests useful add-ons and cross-sell products.

⬇️

**7. 🚨 Escalation Agent**  
Prepares a supervisor hand-off when RetailAI cannot resolve
the customer's request.
""")

st.divider()


# -------------------------------------------------
# LOAD ORCHESTRATOR AGENT
# -------------------------------------------------

@st.cache_resource
def load_agent():
    return OrchestratorAgent()


agent = load_agent()


# -------------------------------------------------
# CUSTOMER QUERY
# -------------------------------------------------

st.subheader("💬 Customer Requirement")

user_query = st.text_area(
    "Enter the customer's request:",
    placeholder=(
         "Describe what the customer is looking for — "
        "product, brand, color, size and budget."
    ),
    height=100
)


# -------------------------------------------------
# ASK RETAILAI BUTTON
# -------------------------------------------------

if st.button("🔍 Ask RetailAI", type="primary"):

    if not user_query.strip():

        st.warning("Please enter a customer request.")

    else:

        try:

            with st.spinner(
                "RetailAI agents are analyzing the request..."
            ):

                result = agent.process_request(user_query)

            st.success("Analysis completed!")


            # -------------------------------------------------
            # AGENT ACTIVITY
            # -------------------------------------------------

            st.subheader("🤖 Agent Activity")

            st.write(
                "✅ Product Query Agent — Customer request understood"
            )

            st.write(
                "✅ Orchestrator Agent — Request routing completed"
            )

            st.write(
                "✅ Inventory Agent — Inventory checked"
            )


            # If product is available
            if result["product_found"]:

                st.write(
                    "✅ Promotion Agent — Promotions checked"
                )

                st.write(
                    "✅ Personalization Agent — Add-ons generated"
                )

                st.write(
                    "⏸️ Recommendation Agent — Not required"
                )

                st.write(
                    "⏸️ Escalation Agent — Not required"
                )


            # If product is unavailable
            else:

                alternatives = result["alternatives"]

                st.write(
                    "✅ Recommendation Agent — Alternatives checked"
                )

                if (
                    alternatives is not None
                    and not alternatives.empty
                ):

                    st.write(
                        "⏸️ Escalation Agent — Not required"
                    )

                else:

                    st.write(
                        "✅ Escalation Agent — "
                        "Supervisor hand-off created"
                    )

            st.divider()


            # -------------------------------------------------
            # AI UNDERSTANDING
            # -------------------------------------------------

            st.subheader("🧠 AI Understanding")

            query_data = result["query_data"]

            col1, col2, col3, col4, col5 = st.columns(5)

            col1.metric(
                "Brand",
                query_data.get("brand") or "Any"
            )

            col2.metric(
                "Category",
                query_data.get("category") or "Any"
            )

            col3.metric(
                "Color",
                query_data.get("color") or "Any"
            )

            col4.metric(
                "Size",
                str(query_data.get("size") or "Any")
            )

            col5.metric(
                "Budget",
                (
                    f"Rs. {query_data.get('max_price')}"
                    if query_data.get("max_price")
                    else "Any"
                )
            )

            st.divider()


            # -------------------------------------------------
            # PRODUCT FOUND
            # -------------------------------------------------

            if result["product_found"]:

                product = result["product"]

                st.subheader("✅ Product Available")

                st.write(
                    f"### {product['product_name']}"
                )

                c1, c2, c3 = st.columns(3)


                # Product information - Column 1

                c1.write(
                    f"**Brand:** {product['brand']}"
                )

                c1.write(
                    f"**Category:** {product['category']}"
                )


                # Product information - Column 2

                c2.write(
                    f"**Color:** {product['color']}"
                )

                c2.write(
                    f"**Size:** {product['size']}"
                )


                # Product information - Column 3

                c3.write(
                    f"**Stock:** {product['stock']}"
                )

                c3.write(
                    f"**Rating:** {product['rating']} ⭐"
                )


                st.write(
                    f"**Original Price:** "
                    f"Rs. {product['price']:.2f}"
                )


                # -------------------------------------------------
                # PROMOTION
                # -------------------------------------------------

                promotion = result["promotion"]

                if promotion["promotion_available"]:

                    st.subheader("🏷️ Promotion Available")

                    st.success(
                        promotion["description"]
                    )

                    p1, p2, p3 = st.columns(3)

                    p1.metric(
                        "Discount",
                        f"{promotion['discount_percent']}%"
                    )

                    p2.metric(
                        "You Save",
                        f"Rs. {promotion['discount_amount']}"
                    )

                    p3.metric(
                        "Final Price",
                        f"Rs. {promotion['final_price']}"
                    )

                else:

                    st.info(
                        "No promotion is currently "
                        "available for this product."
                    )


                # -------------------------------------------------
                # PERSONALIZED ADD-ONS
                # -------------------------------------------------

                addons = result["addons"]

                if (
                    addons is not None
                    and not addons.empty
                ):

                    st.subheader(
                        "🛒 Recommended Add-ons"
                    )

                    st.write(
                        "RetailAI recommends these products "
                        "to complement the customer's purchase."
                    )

                    st.dataframe(
                        addons[
                            [
                                "product_name",
                                "brand",
                                "category",
                                "price",
                                "rating"
                            ]
                        ],
                        use_container_width=True,
                        hide_index=True
                    )


            # -------------------------------------------------
            # PRODUCT NOT FOUND
            # -------------------------------------------------

            else:

                st.warning(
                    "The exact requested product "
                    "is currently unavailable."
                )

                alternatives = result["alternatives"]


                # -------------------------------------------------
                # ALTERNATIVE PRODUCTS
                # -------------------------------------------------

                if (
                    alternatives is not None
                    and not alternatives.empty
                ):

                    st.subheader(
                        "💡 Suggested Alternatives"
                    )

                    st.write(
                        "RetailAI found the following "
                        "suitable alternatives:"
                    )

                    st.dataframe(
                        alternatives[
                            [
                                "product_name",
                                "brand",
                                "color",
                                "size",
                                "price",
                                "stock",
                                "rating"
                            ]
                        ],
                        use_container_width=True,
                        hide_index=True
                    )


                # -------------------------------------------------
                # ESCALATION
                # -------------------------------------------------

                if result["escalation"]:

                    escalation = result["escalation"]

                    st.subheader(
                        "🚨 Supervisor Escalation"
                    )

                    st.error(
                        escalation["message"]
                    )

                    st.write(
                        "**Reason:**",
                        escalation["reason"]
                    )

                    st.write(
                        "**Attempted Solution:**",
                        escalation[
                            "attempted_solution"
                        ]
                    )


        # -------------------------------------------------
        # ERROR HANDLING
        # -------------------------------------------------

        except Exception as e:

            st.error(
                "RetailAI encountered an error "
                "while processing the request."
            )

            st.write(
                "Please try again. If the problem continues, "
                "check the Gemini API connection."
            )

            with st.expander("Technical Error Details"):

                st.code(str(e))