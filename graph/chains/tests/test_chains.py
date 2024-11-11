
from graph.chains.classifier import classifier, ClassifyDocuments
from graph.chains.retrieval_grader import retrieval_grader,GradeDocuments
from ingestion import retriever_legal_doc, retriever_other



def test_classifier()->None:
    question = "what type of document is this"
    docs = retriever_legal_doc.invoke(question)
    res: ClassifyDocuments = classifier.invoke(
            {
                "document": docs,
            }
        )
    print (res)

def test_retrieval_grader_answer_yes():
    question="acceptability criteria"
    doc_1=retriever_legal_doc.invoke(question)
    doc_2 = retriever_other.invoke(question)
    docs=doc_1+doc_2
    doc_txt=[doc.page_content for doc in docs]

    res: GradeDocuments = retrieval_grader.invoke(
        {
            "question": question,
            "document": doc_txt
        }
    )

    assert res.binary_score=="yes"

def test_retrieval_grader_answer_no():
    question="Is how i met your mother a bad or a good tv show"
    doc_1=retriever_legal_doc.invoke(question)
    doc_2 = retriever_other.invoke(question)
    docs=doc_1+doc_2
    doc_txt=[doc.page_content for doc in docs]

    res: GradeDocuments = retrieval_grader.invoke(
        {
            "question": question,
            "document": doc_txt
        }
    )

    assert res.binary_score=="no"