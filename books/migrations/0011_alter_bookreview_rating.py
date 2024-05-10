# Generated by Django 5.0.2 on 2024-05-09 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_bookreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookreview',
            name='rating',
            field=models.CharField(choices=[('Very Good', 'Very good'), ('Good', 'Good'), ('Worth to Read', 'Worth to Read'), ('Bad', 'Bad'), ('Very Bad', 'Very bad')], max_length=15),
        ),
    ]