import csv
from datetime import datetime
from .models import Post
import json

def load_data_from_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            text = row['text']
            created_date = datetime.strptime(row['created_date'], '%Y-%m-%d %H:%M:%S')
            rubrics = row['rubrics'][1:-1].split(", ")
            rubrics = [rubric.strip("'") for rubric in rubrics]
            post = Post.objects.create(text=text, created_date=created_date, rubrics=rubrics)
            post.save()
 
