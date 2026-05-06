from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

def index_document(doc):
    es.index(
        index="documents",
        id=doc.id,
        body={
            "name": doc.name,
            "content": doc.content,
            "type": "file",
        }
    )


def search_documents(query):
    return es.search(
        index="documents",
        body={
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["name", "content"]
                }
            }
        }
    )