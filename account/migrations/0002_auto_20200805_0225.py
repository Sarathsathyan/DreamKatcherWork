# Generated by Django 3.0.9 on 2020-08-05 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermore',
            name='u_id',
            field=models.IntegerField(null=True),
        ),
    ]
