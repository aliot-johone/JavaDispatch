# Generated by Django 2.1.4 on 2019-01-04 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jdfile', '0003_auto_20190103_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='jdfile',
            name='status',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
