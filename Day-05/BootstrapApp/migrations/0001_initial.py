# Generated by Django 3.0 on 2022-11-04 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stroll', models.CharField(max_length=50)),
                ('stname', models.CharField(max_length=80)),
                ('stbranch', models.CharField(max_length=20)),
                ('styear', models.IntegerField()),
            ],
        ),
    ]