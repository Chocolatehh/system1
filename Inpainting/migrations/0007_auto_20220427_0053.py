# Generated by Django 3.1.3 on 2022-04-26 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inpainting', '0006_auto_20220426_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='edge_path',
            field=models.CharField(default='/static/media/edge.jpg', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='masked_path',
            field=models.CharField(default='/static/media/masked.jpg', max_length=255),
        ),
    ]