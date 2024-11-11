from typing import Any, Dict
from graph.chains.classifier import classifier
from graph.state import GraphState


def classify(state:GraphState)->Dict[str,Any]:

    """
    Determines what type of document we are analyzing (Contract, Agreement, NDA, ...)

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): Filtered out irrelevant documents and updated web_search state
    """

    print("--CLASSIFY DOCUMENT TO BE ANALYZED--")
    question = state["question"]
    documents_analyzed = state["documents_analyzed"]
    documents_other=state["documents_other"]
    legal_type=classifier.invoke({"documents":documents_analyzed})

    return {"question": question, "documents_analyzed": documents_analyzed, "documents_other": documents_other, "legal_doc_type":legal_type}