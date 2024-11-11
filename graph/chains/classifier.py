from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI
from ingestion import retriever_legal_doc

from graph.state import GraphState

model='gpt-4o'
llm = ChatOpenAI(model_name=model,temperature=0)

class ClassifyDocuments(BaseModel):
    """Binary score for relevance check on retrieved documents."""

    answer: str = Field(
        description="What type of legal document is the document uploaded."
    )

structured_llm_grader = llm.with_structured_output(ClassifyDocuments)

system = """You are a legal expert assessing the type of document that was uploaded.  \n
    Give an answer with the type of legal document ."""

classify_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "Retrieved document: \n\n {documents}"),
    ]
)

classifier= classify_prompt | structured_llm_grader







