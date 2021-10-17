# Generated by Django 2.2.10 on 2021-10-17 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_delete_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField(verbose_name='ID пользователя')),
                ('answer_text', models.TextField(blank=True, max_length=500, null=True, verbose_name='Тектс ответа')),
                ('choice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='polls.Choice', verbose_name='Выбранный вариант ответа')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='polls.Poll', verbose_name='Опрос')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='polls.Question', verbose_name='Вопрос')),
            ],
            options={
                'verbose_name': 'ответ',
                'verbose_name_plural': 'ответы',
            },
        ),
    ]