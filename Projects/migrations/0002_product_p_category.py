# Generated by Django 4.2 on 2023-04-16 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='p_category',
            field=models.CharField(default='', max_length=50),
        ),
    ]
