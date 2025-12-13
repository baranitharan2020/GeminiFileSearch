from google import genai

client = genai.Client(api_key="") # Add your Gemini API key Here

# List all file-search stores
stores = client.file_search_stores.list()
for s in stores:
    print("Store name:", s.name, " Display name:", s.display_name,
          "Active docs:", getattr(s, 'active_documents_count', None))