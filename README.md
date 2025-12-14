# Gemini File Search – RAG as a Service (Google ADK)

This repository demonstrates how to use **Gemini File Search** with **Google ADK** to build a simplified RAG (Retrieval-Augmented Generation) workflow and an interactive AI agent.

The project covers:
- Creating and managing File Search Stores
- Uploading documents
- Querying documents using a File Search Store ID
- Running an AI agent for interactive document Q&A

---

## Repository Structure

```
.
├── file_search_store.py
├── file_store_query.py
├── list_file_store_ids.py
├── search_agent/
│   └── (AI Agent implementation)
└── README.md
```

### File Descriptions

- **file_search_store.py**  
  Uploads a document to the Gemini File Search Store and creates a File Search Store.

- **file_store_query.py**  
  Queries the uploaded documents using a File Search Store ID.

- **list_file_store_ids.py**  
  Lists all available File Search Stores associated with the API key.

- **search_agent/**  
  Contains the AI Agent implementation built using Google ADK for interactive querying.

---

## Prerequisites

- Python 3.9 or later  
- Google ADK installed on your system  
- A valid Gemini API key  

---

## Setup Instructions

### 1. Install Google ADK

```bash
pip install google-adk
```

### 2. Configure Environment Variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## Usage

### 1. Create a File Search Store and Upload a File

```bash
python file_search_store.py
```

Save the **File Search Store ID** printed in the output for future use.

---

### 2. Query the File Search Store

```bash
python file_store_query.py
```

---

### 3. List Available File Search Stores

```bash
python list_file_store_ids.py
```

---

## Running the AI Agent

The `search_agent` folder contains an AI Agent built using Google ADK.

### Steps
1. Launch the Google ADK web interface  
2. Start the File Search Agent  
3. Provide the file path or File Search Store ID in the chat  
4. Ask questions interactively based on the uploaded documents  

---

## Key Features

- Managed RAG using Gemini File Search  
- Automatic chunking, embedding, and semantic retrieval  
- No manual vector database management  
- Interactive AI agent using Google ADK  

---

## License

Creative Commons Attribution 4.0 International (CC BY 4.0)
