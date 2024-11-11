from typing import List, TypedDict


class GraphState(TypedDict):
    """
    Represents the state of our graph.

    Attributes:
        question: question
        generation: LLM generation
        legañl_doc_type: Type of legal document (NDA, Contract, Agreement,...)
        web_search: whether to add search
        documents: list of documents
    """

    question: str
    question_summarized:str
    generation: str
    legal_doc_type:str
    web_search: bool
    documents_analyzed: List[str]
    documents_other: List[str]
    documents_filtered: List[str]
