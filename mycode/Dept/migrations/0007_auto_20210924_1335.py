# Generated by Django 3.2.7 on 2021-09-24 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dept', '0006_ss'),
    ]

    operations = [
        migrations.AddField(
            model_name='ss',
            name='ref_cb',
            field=models.FloatField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ss',
            name='ref_cf',
            field=models.FloatField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ss',
            name='ref_cw',
            field=models.FloatField(blank=True, max_length=200, null=True),
        ),
    ]
