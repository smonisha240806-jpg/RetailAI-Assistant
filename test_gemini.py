import os
from dotenv import load_dotenv
from google import genai


# Load environment variables from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("ERROR: Gemini API key not found.")

else:
    try:
        client = genai.Client(api_key=api_key)

        chat = client.chats.create(
            model="gemini-3.8-flash"
        )

        response = chat.send_message(
            "Say exactly: RetailAI Gemini connection successful!"
        )

        print("\nGemini Response:\n")
        print(response.text)

    except Exception as e:
        print("\nGemini Error:")
        print(e)