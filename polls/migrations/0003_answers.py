# Generated by Django 2.2.10 on 2021-10-16 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20211016_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField(verbose_name='ID пользователя')),
                ('answer_text', models.TextField(max_length=500, verbose_name='Текст ответа')),
                ('answer_choice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Choice', verbose_name='Выбранный вариант ответа')),
            ],
            options={
                'verbose_name': 'ответ',
                'verbose_name_plural': 'ответы',
            },
        ),
    ]