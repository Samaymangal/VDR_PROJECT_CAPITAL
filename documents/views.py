from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Document
from .tasks import process_document
from .search import search_documents



class UploadDocumentView(APIView):
    def post(self, request):
        file = request.FILES['file']
        folder_id = request.data.get('folder')

        doc = Document.objects.create(
            name=file.name,
            file=file,
            folder_id=folder_id
        )

        process_document.delay(doc.id)

        return Response({"message": "Uploaded"})


class SearchView(APIView):
    def get(self, request):
        query = request.GET.get('q', '').lower().strip()

        results = search_documents(query)

        return Response(results)
    

from .tasks import index_document_task

def upload_document(request):
    if request.method == "POST":
        # your existing save logic
        doc = form.save()

        # 🔥 Trigger async indexing
        index_document_task.delay(doc.id)

        return redirect("success")