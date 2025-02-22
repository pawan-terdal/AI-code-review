from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI()
prompt_context = """
Review the following code and suggest improvements. Make sure you respond in less than 100 words at any cost.
Dont focus on trivial things. Focus mostly on logic, industry standards. Return in the tone of a senior engineer, 
be a little casual and dont be too formal \n\n"


"""
def analyze_code_with_ai(code_snippet):
    """Uses GPT-4 to analyze code and suggest improvements."""
    prompt = prompt_context + code_snippet

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content

def foo():
    print("you suck")

if __name__ == "__main__":
    sample_code = """def add(a, b): return a+b"""
    print(analyze_code_with_ai(sample_code))
