import os
import json
import time

from dotenv import load_dotenv
from google import genai


class ProductQueryAgent:

    def __init__(self):

        load_dotenv()

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY not found in .env file"
            )

        self.client = genai.Client(
            api_key=api_key
        )

        self.chat = self.client.chats.create(
            model="gemini-3.8-flash"
        )


    def understand_query(self, user_query):

        prompt = f"""
You are the Product Query Agent for a retail store.

Your job is to understand the store associate's request
and extract product search information.

Return ONLY valid JSON.

Use this exact structure:

{{
    "brand": null,
    "category": null,
    "color": null,
    "size": null,
    "max_price": null
}}

Rules:

1. brand should contain the requested brand such as
   Nike, Adidas or Puma.

2. category should contain values such as:
   Running Shoes
   Casual Shoes
   Socks
   T-Shirt
   Shorts
   Backpack
   Accessories

3. color should contain the requested color.

4. size should contain the requested size.

5. max_price should contain only the numeric
   maximum budget.

6. If information is not mentioned, use null.

7. Do not include explanations.

Store associate request:

{user_query}
"""

        max_attempts = 3

        for attempt in range(max_attempts):

            try:

                response = self.chat.send_message(
                    prompt
                )

                response_text = response.text.strip()

                # Remove Markdown formatting
                # if Gemini returns ```json
                if response_text.startswith("```"):

                    response_text = response_text.replace(
                        "```json",
                        ""
                    )

                    response_text = response_text.replace(
                        "```",
                        ""
                    )

                    response_text = response_text.strip()

                return json.loads(response_text)


            except Exception as e:

                error_message = str(e)

                # Retry only for temporary server errors
                if (
                    "503" in error_message
                    or "UNAVAILABLE" in error_message
                    or "high demand" in error_message.lower()
                ):

                    if attempt < max_attempts - 1:

                        wait_time = 2 * (attempt + 1)

                        print(
                            f"Gemini temporarily unavailable. "
                            f"Retrying in {wait_time} seconds..."
                        )

                        time.sleep(wait_time)

                    else:

                        raise Exception(
                            "Gemini is temporarily busy. "
                            "Please try again in a few moments."
                        )

                else:

                    # Other errors should not be retried
                    raise