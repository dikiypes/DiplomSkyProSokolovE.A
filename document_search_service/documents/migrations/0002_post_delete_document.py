# Generated by Django 5.0.6 on 2024-05-11 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField()),
                ('rubrics', models.JSONField()),
            ],
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]