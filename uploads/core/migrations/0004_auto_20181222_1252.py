# Generated by Django 2.1.3 on 2018-12-22 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_document_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
