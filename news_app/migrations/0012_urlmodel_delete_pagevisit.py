# Generated by Django 5.1.6 on 2025-02-09 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0011_rename_url_pagevisit_url_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='URLModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('visits', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='PageVisit',
        ),
    ]
