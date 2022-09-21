# Generated by Django 4.0.4 on 2022-09-13 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0004_rename_serverity_disease_severity'),
        ('hardwarecontrols', '0002_hardwaresession_sessionimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessionimage',
            name='disease_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='prediction.disease'),
        ),
    ]
