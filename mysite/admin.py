from django.contrib import admin
from .models import MainContent, Comment

class MainContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'pub_date'] # 출력할 필드 정의
    search_fields = ['title'] # title 기준으로 검색

class CommentAdmin(admin.ModelAdmin):
    list_display = ['content_list', 'content', 'author', 'create_date', 'modify_date'] # 출력할 필드 정의
    search_fields = ['author'] # author 기준으로 검색

# Register your models here.
admin.site.register(MainContent, MainContentAdmin)
admin.site.register(Comment, CommentAdmin)


