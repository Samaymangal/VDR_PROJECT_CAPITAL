from celery import shared_task
from .models import Document
from .utils import extract_content
from .search import index_document

@shared_task
def process_document(doc_id):
    doc = Document.objects.get(id=doc_id)

    # Extract content
    content = extract_content(doc.file.path)
    doc.content = content
    doc.save()

    # Index to Elasticsearch
    index_document(doc)

from celery import shared_task
from elasticsearch import Elasticsearch
from .models import Document

es = Elasticsearch("http://localhost:9200")

@shared_task
def index_document_task(doc_id):
    try:
        doc = Document.objects.get(id=doc_id)

        es.index(
            index="documents",
            id=doc.id,
            body={
                "name": doc.name,
                "content": doc.content,
                "type": "file",
            }
        )

        return f"Indexed document {doc_id}"

    except Document.DoesNotExist:
        return f"Document {doc_id} not found"