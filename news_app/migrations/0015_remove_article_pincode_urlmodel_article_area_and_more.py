# Generated by Django 5.1.6 on 2025-03-15 18:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0014_article_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='pincode',
        ),
        migrations.AddField(
            model_name='urlmodel',
            name='article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='news_app.article'),
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('articles', models.ManyToManyField(related_name='areas', to='news_app.article')),
                ('posts', models.ManyToManyField(related_name='areas', to='news_app.post')),
            ],
        ),
        migrations.AddField(
            model_name='urlmodel',
            name='area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='news_app.area'),
        ),
    ]
