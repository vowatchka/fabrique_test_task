# Generated by Django 2.2.10 on 2021-10-16 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20211016_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_text',
            field=models.TextField(max_length=500, null=True, verbose_name='Текст ответа'),
        ),
    ]