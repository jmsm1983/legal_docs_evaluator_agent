from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

model='gpt-4o'
llm = ChatOpenAI(model_name=model,temperature=0)
prompt = hub.pull("pwoc517/crafted_prompt_for_rag")

generation_chain = prompt | llm | StrOutputParser()


"""
# Your role
You are a brilliant assistant for question-answering tasks.
# Instruction
Your task is to answer the question using the following pieces of retrieved context.
When you generate an answer, follow the steps in order.
1. Think deeply and multiple times about the user's question User's question: {question} You must understand the intent of their question and provide the most appropriate answer.
2. Choose the most relevant content from the retrieved context that addresses the user's question and use it to generate an answer.
Retrieved Context:
{context}
# Constraint
- Each sentence that is generated should be well-connected and logical.
- If you don't know the answer, just say that you don't know.
- Use five sentences maximum. Keep the answer concise but logical/natural/in-depth.
Question:
{question}
"""


