from django.contrib import admin
from .models import Folder,Files

# admin.site.register(Files)
# admin.site.register(Folder)

# from django.contrib import admin
# from .models import Files, Folder

@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):
    list_display = ['name', 'file_type', 'folder', 'user', 'uploaded_at']  # show columns
    list_filter = ['file_type', 'uploaded_at', 'folder']                   # right sidebar filters
    search_fields = ['name', 'user__username']                             # search bar
    ordering = ['-uploaded_at']                                            # newest first
    list_per_page = 20                                                     # pagination
    date_hierarchy = 'uploaded_at'                                         # date drill-down

@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent']
    search_fields = ['name']


# @admin.register(Files)
# class FileAdmin(admin.ModelAdmin):
#     list_display = ('name', 'user', 'uploaded_at')

#     def save_model(self, request, obj, form, change):
#         if not obj.user:
#             obj.user = request.user
#         super().save_model(request, obj, form, change)