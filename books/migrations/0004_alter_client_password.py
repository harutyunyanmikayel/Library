# Generated by Django 5.0.2 on 2024-04-29 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_client_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]
