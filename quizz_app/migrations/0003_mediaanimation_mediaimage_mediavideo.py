# Generated by Django 5.1.6 on 2025-06-11 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizz_app', '0002_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaAnimation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('animation', models.FileField(upload_to='animations/')),
            ],
        ),
        migrations.CreateModel(
            name='MediaImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='MediaVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('video', models.FileField(upload_to='videos/')),
            ],
        ),
    ]
