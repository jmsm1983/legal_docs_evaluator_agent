from typing import Any, Dict
from graph.chains.generation import generation_chain
from graph.state import GraphState


def generate(state:GraphState)->Dict[str,Any]:

    """
    Determines whether the retrieved documents are relevant to the question
    If any document is not relevant, we will set a flag to run web search

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): Filtered out irrelevant documents and updated web_search state
    """

    print("--GENERATE ANSWER--")
    question = state["question"]
    try:
        documents_filtered = state["documents_filtered"]
    except:
        documents_filtered =[]

    answer=generation_chain.invoke({"context":documents_filtered, "question":question})

    return {"documents_filtered": documents_filtered, "question": question, "generation":answer}