from typing import Any, Dict

from langchain.schema import Document
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import ChatPromptTemplate
from graph.state import GraphState
from langchain_openai import ChatOpenAI

web_search_tool = TavilySearchResults(k=3)

model='gpt-4o'
llm = ChatOpenAI(model_name=model,temperature=0.1)

def summarize_question(question, legal_doc_type):

    question= question
    legal_doct_type=legal_doc_type


    # Define system instructions for relevance check and concise question summarization
    system_instructions = """You are an AI assistant with the task of summarizing questions.
        If the question is related to legal issues you will be provided with the question and  the type fo legal document. Otherwise the type of legal document will be empty.
        If the question provided is long, summarize it concisely max 15 words to make it searchable. If not, keep it as is.
        try to keep it as a question
        """

    # Define prompt template for summarizing the question and assessing relevance
    summarize_question_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_instructions),
            ("human", f"question:\n\n{question}\n\nType of legal document: {legal_doc_type}\n\n"),
        ]
    )

    # Generate summarized question and relevance check output
    messages = summarize_question_prompt.format_messages()
    response = llm.invoke(input=messages)
    return response.content


def web_search(state: GraphState) -> Dict[str, Any]:
    print("--WEB SEARCH--")


    question = state["question"]
    try:
        legal_doc_type=state["legal_doc_type"]
    except:
        legal_doc_type = ""

    try:
        documents_filtered = state["documents_filtered"]
    except:
        documents_filtered = []

    summarized_question=summarize_question(question, legal_doc_type)
    print (summarized_question)

    docs = web_search_tool.invoke({"query": summarized_question})
    web_results = "\n".join([d["content"] for d in docs])
    web_results = Document(page_content=web_results)

    if documents_filtered is not None:
        documents_filtered.append(web_results)
    else:
        documents_filtered = [web_results]
    return {"documents_filtered": documents_filtered, "question_summarized": summarized_question}
