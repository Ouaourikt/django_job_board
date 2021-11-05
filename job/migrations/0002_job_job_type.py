# Generated by Django 3.2.9 on 2021-11-05 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Full time', 'Full time'), ('Part time', 'Part time')], default='', max_length=15),
            preserve_default=False,
        ),
    ]
