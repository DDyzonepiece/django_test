# Generated by Django 2.2.7 on 2019-11-17 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_choice_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='pub_data',
            new_name='pub_date',
        ),
    ]