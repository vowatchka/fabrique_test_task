# Generated by Django 2.2.10 on 2021-10-16 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='choice',
            options={'verbose_name': 'вариант ответа', 'verbose_name_plural': 'варианты ответов'},
        ),
        migrations.AlterModelOptions(
            name='poll',
            options={'verbose_name': 'опрос', 'verbose_name_plural': 'опросы'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'вопрос', 'verbose_name_plural': 'вопросы'},
        ),
    ]
