# Generated by Django 3.2.7 on 2021-09-22 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FtTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_date', models.DateField()),
                ('test_business', models.CharField(max_length=200)),
                ('test_product', models.CharField(max_length=200)),
                ('test_pac', models.CharField(max_length=200)),
                ('test_person', models.CharField(max_length=200)),
                ('test_site', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CALL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('call_operator', models.DateField()),
                ('call_terminal', models.CharField(max_length=200)),
                ('call_direction', models.CharField(max_length=200)),
                ('call_environment', models.CharField(max_length=200)),
                ('call_vonr', models.CharField(max_length=200)),
                ('call_epsfb', models.CharField(max_length=200)),
                ('call_volte', models.CharField(max_length=200)),
                ('call_csfb', models.CharField(max_length=200)),
                ('fttest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dept.fttest')),
            ],
        ),
    ]