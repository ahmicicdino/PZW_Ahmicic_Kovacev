# Generated by Django 4.1.3 on 2022-12-22 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_author_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Broj telefona'),
        ),
    ]