from google import genai
from google.genai import types

api_key = "" # Add your Gemini API key Here   
client = genai.Client(api_key=api_key)

file_search_store_id = "fileSearchStores/productdocuments-lc8rbxxxxxxx"  # Replace with your File Search Store ID

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain about the BYD Assistant?",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                file_search=types.FileSearch(
                    file_search_store_names=[file_search_store_id]
                )
            )
        ]
    )
)

print(response.text)
