# from django_elasticsearch_dsl import Document, Index
# from .models import File

# file_index = Index('files')

# @file_index.doc_type
# class FileDocument(Document):
#     class Django:
#         model = File
#         fields = [
#             'name',
#             'file_type',
#         ]