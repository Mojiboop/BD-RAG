import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Please input your api key into .env")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents="""Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.""",
    )
usage = response.usage_metadata

if not usage:
    raise RuntimeError("Gemini API response appears to be missing usage metadata")

print(f"Prompt tokens: {usage.prompt_token_count}")
print(f"Response tokens: {usage.candidates_token_count}")
print(f"Response:\n{response.text}")



#if __name__ == "__main__":
#   main()
