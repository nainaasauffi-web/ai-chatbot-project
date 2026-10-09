import os
from openai import OpenAI

api_key = os.environ.get("OPENAI_API_KEY", "YOUR_API_KEY_HERE")
client = OpenAI(api_key=api_key)

print("🤖 AI Course Tutor Online! (Taip 'exit' untuk keluar)\n")

while True:
    user_input = input("Anda: ")
    if user_input.strip().lower() == "exit":
        print("Selesai! Selamat tinggal.")
        break
    if not user_input.strip():
        continue
        
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an AI tutor helping students understand AI concepts. Explain terms simply and clearly."},
                {"role": "user", "content": user_input}
            ]
        )
        print(f"\nBot: {response.choices.message.content}\n")
    except Exception as e:
        print(f"\nSila tetapkan API Key untuk berbual. (Error: {e})\n")
