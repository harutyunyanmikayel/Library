# Generated by Django 5.0.2 on 2024-05-09 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_alter_bookreview_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookreview',
            name='rating',
            field=models.CharField(choices=[('Great', 'Great'), ('Good', 'Good'), ('Decent', 'Decent'), ('Bad', 'Bad'), ('Terrible', 'Terrible')], max_length=15),
        ),
    ]
