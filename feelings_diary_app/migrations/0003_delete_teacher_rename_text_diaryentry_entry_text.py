# Generated by Django 4.2 on 2023-04-22 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feelings_diary_app', '0002_diaryentry'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Teacher',
        ),
        migrations.RenameField(
            model_name='diaryentry',
            old_name='text',
            new_name='entry_text',
        ),
    ]