# Generated by Django 2.1.4 on 2018-12-28 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('server', models.IntegerField()),
                ('remark', models.CharField(max_length=1000)),
                ('status', models.IntegerField()),
            ],
        ),
    ]