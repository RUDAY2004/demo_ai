from groq import Groq

# Directly pass the API key into the Groq client instead of using os.environ
client = Groq(api_key="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")

def get_response(prompt):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="llama3-8b-8192"
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error fetching response: {e}"
