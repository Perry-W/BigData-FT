# Generated by Django 3.2.7 on 2021-09-22 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dept', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='call_operator',
            field=models.CharField(max_length=200),
        ),
    ]
