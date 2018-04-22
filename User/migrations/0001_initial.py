# Generated by Django 2.0.4 on 2018-04-20 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=20)),
                ('mail', models.CharField(max_length=25)),
                ('points_total', models.IntegerField()),
                ('points_monthly', models.IntegerField()),
            ],
        ),
    ]