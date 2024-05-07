# Generated by Django 5.0.2 on 2024-05-07 10:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_delete_bookreview'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=500)),
                ('rating', models.CharField(choices=[('EXCELLENT', 'Excellent'), ('GOOD', 'Good'), ('NORMAL', 'Normal'), ('BAD', 'Bad'), ('TERRIBLE', 'Terrible')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.client')),
            ],
        ),
    ]