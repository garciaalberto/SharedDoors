# Generated by Django 2.0.4 on 2018-05-07 13:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0005_auto_20180501_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.CharField(choices=[('M', 'Menu'), ('T', 'Task'), ('P', 'Payment'), ('B', 'Birthday')], default=django.utils.timezone.now, max_length=1),
            preserve_default=False,
        ),
    ]
