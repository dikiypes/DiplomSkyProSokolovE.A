# -*- coding: utf-8 -*-
from .models import Post
from .documents_indexes import PostDocument

def search_posts(query):
    search = PostDocument.search().query("match", text=query)[:20]
    qs = search.to_queryset().order_by('created_date')

    return qs

def delete_post(document_id):
    PostDocument.get(id=document_id).delete()
    Post.objects.get(id=document_id).delete()
 
