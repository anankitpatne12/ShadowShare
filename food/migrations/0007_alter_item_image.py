# Generated by Django 4.1.7 on 2023-05-03 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_alter_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='empty-box.gif', upload_to='posts'),
        ),
    ]
