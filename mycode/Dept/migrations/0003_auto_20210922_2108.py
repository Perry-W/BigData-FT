# Generated by Django 3.2.7 on 2021-09-22 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dept', '0002_alter_call_call_operator'),
    ]

    operations = [
        migrations.RenameField(
            model_name='call',
            old_name='call_direction',
            new_name='call_business_direction_ter',
        ),
        migrations.RemoveField(
            model_name='call',
            name='call_terminal',
        ),
    ]