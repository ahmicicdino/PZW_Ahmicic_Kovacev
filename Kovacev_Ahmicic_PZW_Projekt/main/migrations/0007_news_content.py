# Generated by Django 4.1.3 on 2022-12-20 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_category_news_delete_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Tekst članka'),
        ),
    ]
