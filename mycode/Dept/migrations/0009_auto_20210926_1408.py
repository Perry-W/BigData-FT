# Generated by Django 3.2.7 on 2021-09-26 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dept', '0008_ttff'),
    ]

    operations = [
        migrations.AddField(
            model_name='ttff',
            name='test_hdware',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ttff',
            name='test_pac',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ttff',
            name='test_product',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ttff',
            name='test_state',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
