# Generated by Django 4.2 on 2023-04-16 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_title', models.CharField(max_length=50)),
                ('skill_percentage', models.CharField(max_length=50)),
                ('skill_category', models.CharField(max_length=50)),
            ],
        ),
    ]
