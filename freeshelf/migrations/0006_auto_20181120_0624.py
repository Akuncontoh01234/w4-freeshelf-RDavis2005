# Generated by Django 2.1.3 on 2018-11-20 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freeshelf', '0005_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.FileField(blank=True, default='default.png', upload_to=''),
        ),
    ]
