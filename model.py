import google.generativeai as genai

genai.configure(api_key="AIzaSyAtjvXqC9Lb87fvKlytD0NIEkGLnzefBng")
client = genai.GenerativeModel("gemini-2.0-flash")

def llm_generate(prompt):
    response = client.generate_content(prompt)
    return response.text.strip()
