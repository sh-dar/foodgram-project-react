# Generated by Django 3.2.16 on 2024-05-11 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_auto_20240508_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Продукт'),
        ),
    ]
