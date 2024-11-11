from typing import Any, Dict

from graph.state import GraphState
from ingestion import retriever_legal_doc,retriever_other

# Define the retrieve function, which takes a GraphState object and returns a dictionary

def retrieve(state:GraphState)-> Dict[str, Any]:
    print ("--RETRIEVE LEGAL DOC--")
    question=state["question"]
    documents_analyzed=retriever_legal_doc.invoke(question)
    documents_other = retriever_legal_doc.invoke(question)
    return {"documents_analyzed": documents_analyzed,"documents_other": documents_other, "question": question}





"""
if __name__=="__main__":
    state: GraphState = {
        "question": "acceptability criteria",  # Set the question to test the retrieve function
        "generation": "",  # Leave generation empty initially
        "web_search": False,  # Set to False for this test
        "documents": []  # Start with an empty list of documents
    }

    result= retrieve(state)
    print ("Retrieve Output", result)

"""