# Generated by Django 5.1.3 on 2024-11-30 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaiverity',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
