# Generated by Django 3.2.7 on 2021-09-26 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dept', '0009_auto_20210926_1408'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ttff',
            old_name='dut1',
            new_name='dut1_acc_ave',
        ),
        migrations.RenameField(
            model_name='ttff',
            old_name='dut2',
            new_name='dut1_acc_cep68',
        ),
        migrations.RenameField(
            model_name='ttff',
            old_name='ref',
            new_name='dut1_acc_cep95',
        ),
        migrations.AddField(
            model_name='ttff',
            name='dut1_acc_max',
            field=models.FloatField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ttff',
            name='dut1_ttff_ave',
            field=models.FloatField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ttff',
            name='dut1_ttff_cep68',
            field=models.FloatField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ttff',
            name='dut1_ttff_cep95',
            field=models.FloatField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ttff',
            name='dut1_ttff_max',
            field=models.FloatField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ttff',
            name='dut2_acc_ave',
            field=models.FloatField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ttff',
            name='dut2_acc_cep68',
            field=models.FloatField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ttff',
            name='dut2_acc_cep95',
            field=models.FloatField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ttff',
            name='dut2_acc_max',
            field=models.FloatField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ttff',
            name='dut2_ttff_ave',
            field=models.FloatField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ttff',
            name='dut2_ttff_cep68',
            field=models.FloatField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ttff',
            name='dut2_ttff_cep95',
            field=models.FloatField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ttff',
            name='dut2_ttff_max',
            field=models.FloatField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ttff',
            name='ref_acc_ave',
            field=models.FloatField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ttff',
            name='ref_acc_cep68',
            field=models.FloatField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ttff',
            name='ref_acc_cep95',
            field=models.FloatField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ttff',
            name='ref_acc_max',
            field=models.FloatField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ttff',
            name='ref_ttff_ave',
            field=models.FloatField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ttff',
            name='ref_ttff_cep68',
            field=models.FloatField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ttff',
            name='ref_ttff_cep95',
            field=models.FloatField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ttff',
            name='ref_ttff_max',
            field=models.FloatField(blank=True, max_length=200, null=True),
        ),
    ]