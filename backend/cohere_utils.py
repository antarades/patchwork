import cohere
import os
from dotenv import load_dotenv
load_dotenv()

co = cohere.Client(os.getenv("COHERE_API_KEY"))
def generate_poetic_reflection(user_input=""):
    if not user_input:
        return "Tell me a little more about how you're feeling."

    prompt = (
        f"A person said: '{user_input}'. "
        f"Write back a single poetic line that reflects, deepens, or gently rephrases their emotional state. "
        f"Be soft, thoughtful, human, and kind."
    )

    try:
        response = co.generate(
            model='command',
            prompt=prompt,
            max_tokens=100,
            temperature=0.8
        )
        return response.generations[0].text.strip()
    except Exception as e:
        print("❌ Error inside generate_poetic_reflection():", e)
        return "Oops! AI is on break."

    return response.generations[0].text.strip()
