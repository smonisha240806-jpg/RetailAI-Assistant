# 🛍️ RetailAI Assistant

## Agentic AI Store Support and Experience Assistant

RetailAI Assistant is an Agentic AI-based digital co-worker designed to help retail store associates quickly respond to customer queries related to products, stock availability, pricing, promotions, alternatives, and personalized recommendations.

The system uses Google Gemini to understand natural-language customer requirements and coordinates multiple specialized agents to determine the appropriate action.

---

## 🎯 Problem Statement

Retail store associates frequently need to answer customer questions such as:

- Is a particular product available?
- Is the required size or color in stock?
- Are there any promotions available?
- What alternatives can be suggested if the product is unavailable?
- What additional products can be recommended?
- When should the request be escalated to a supervisor?

Manually checking all this information can take time and affect the customer experience.

RetailAI Assistant addresses this problem by acting as an intelligent digital co-worker for store associates.

---

## 💡 Proposed Solution

A store associate can enter a natural-language request such as:

> Customer wants black Nike running shoes size 8 under Rs. 5000.

RetailAI automatically:

1. Understands the customer requirement.
2. Extracts product information.
3. Checks available inventory.
4. Checks applicable promotions.
5. Calculates the final discounted price.
6. Suggests alternative products when required.
7. Recommends relevant add-on products.
8. Escalates unresolved requests to a supervisor.

---

## 🤖 Agentic AI Architecture

RetailAI uses multiple specialized agents.

### 🧠 Product Query Agent

Uses Google Gemini to understand natural-language customer requests and extract:

- Brand
- Category
- Color
- Size
- Maximum budget

### 🎯 Orchestrator Agent

Coordinates the complete workflow and decides which specialized agents need to be activated.

### 📦 Inventory Agent

Searches the product inventory and checks product availability based on the customer's requirements.

### 🏷️ Promotion Agent

Checks applicable promotional offers and calculates the discounted final price.

### 💡 Recommendation Agent

Suggests suitable alternative products when the exact requested product is unavailable.

### 🛒 Personalization Agent

Recommends relevant add-ons and cross-sell products.

### 🚨 Escalation Agent

Creates a supervisor hand-off when the customer request cannot be resolved automatically.

---

## 🔄 Workflow

```text
Store Associate
      |
      v
Natural Language Customer Request
      |
      v
Product Query Agent (Gemini)
      |
      v
Orchestrator Agent
      |
      v
Inventory Agent
      |
      +----------------------+
      |                      |
 Product Found          Product Not Found
      |                      |
      v                      v
Promotion Agent       Recommendation Agent
      |                      |
      v                Alternatives Found?
Personalization Agent      /       \
      |                  Yes         No
      v                   |           |
Final Response             v           v
                     Alternatives   Escalation Agent
```

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Google Gemini API
- Google GenAI Python SDK
- Pandas
- python-dotenv
- CSV-based mock retail inventory

---

## 📂 Project Structure

```text
RetailAI_Assistant/
│
├── Agents/
│   ├── __init__.py
│   ├── product_query_agent.py
│   ├── orchestrator_agent.py
│   ├── inventory_agent.py
│   ├── promotion_agent.py
│   ├── recommendation_agent.py
│   ├── personalization_agent.py
│   └── escalation_agent.py
│
├── data/
│   ├── products.csv
│   └── promotions.csv
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Open the project folder

```bash
cd RetailAI_Assistant
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Gemini API Configuration

Create a `.env` file inside the project folder.

Add:

```text
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

The `.env` file is excluded from GitHub using `.gitignore` to protect the API key.

---

## ▶️ Run the Application

Run:

```bash
streamlit run app.py
```

The RetailAI Assistant interface will open in the browser.

---

## 🧪 Demo Scenarios

### Scenario 1 — Product Available

Input:

```text
Customer wants black Nike running shoes size 8 under Rs. 5000
```

Expected behavior:

- Understand customer requirement
- Find Nike Revolution 7
- Check stock
- Apply available promotion
- Calculate discounted price
- Recommend add-ons

### Scenario 2 — Alternative Recommendation

Input:

```text
Customer wants black Nike running shoes size 9 under Rs. 5000
```

Expected behavior:

- Exact requested product unavailable
- Recommendation Agent activated
- Suitable alternative suggested

### Scenario 3 — Supervisor Escalation

Input:

```text
Customer wants white Puma running shoes size 10 under Rs. 3000
```

Expected behavior:

- Requested product unavailable
- No suitable alternatives found
- Escalation Agent activated
- Supervisor hand-off generated

---

## 🔐 Reliability and Security

RetailAI includes:

- Environment-variable-based API key management
- `.gitignore` protection for sensitive credentials
- Gemini temporary server-error retry handling
- Application-level exception handling
- Controlled structured output from Gemini

---

## 🚀 Future Enhancements

Future versions can include:

- Real-time retail inventory APIs
- Customer purchase-history integration
- Voice-based interaction
- Multilingual customer queries
- Store-location-aware inventory
- Advanced customer personalization
- Dynamic pricing and promotion APIs
- Database integration
- Analytics dashboard
- Conversation memory

---

## 🎓 Project Type

Agentic AI / Generative AI / Retail Intelligence

---

## 👩‍💻 Developed By

**Monisha S**  
B.E. Computer Science and Engineering  
Sathyabama University