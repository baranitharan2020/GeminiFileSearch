from google.adk.agents import Agent
from . import filesearch as fs
from typing import Dict, Any

def get_response(question: str, filename: str ) -> Dict[str, Any]:
    result = fs.main(question, filename )
    return {"response": result}

root_agent = Agent(
    name="search_agent",
    model="gemini-2.5-flash",
    description="""
    Greeting the User and ask the user to share the Path of the document to be searched.
    Check the path and pass the file name and path to the file search as `filename` to create a file search store.
    You are an intelligent agent that uses file search to answer questions based on uploaded documents and question asked by the user to be passed as `question`.
    """,
    tools={
        get_response
    }
)