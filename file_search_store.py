from google import genai
from google.genai import types
import time

# Add your Gemini API key Here
api_key = ""  
client = genai.Client(api_key=api_key)

# Create a File Search Store
file_search_store = client.file_search_stores.create(config={'display_name': 'Product_Documents'})  # Name of the File Store

# Upload a document to the File Search Store
operation = client.file_search_stores.upload_to_file_search_store(
  file='BYD.pdf',
  file_search_store_name=file_search_store.name,
  config={
      'display_name' : 'BYD_Manual', # Display name for the uploaded file
  }
)

# Display the File Search Store ID for future reuse
print("File Search Store ID is:", file_search_store.name)

# Wait until the upload and indexing process is complete
while not operation.done:
    time.sleep(5)
    operation = client.operations.get(operation)

# Ask a query that will be answered using the uploaded document
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="""Explain about the Charging colours mentioned in the manual.""",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                file_search=types.FileSearch(
                    file_search_store_names=[file_search_store.name]
                )
            )
        ]
    )
)

print(response.text)