# Generated by Django 4.0.6 on 2023-05-02 06:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('MLProjectApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='type_choice',
            field=models.CharField(choices=[('Feedback', 'Feedback'), ('Query', 'Query')], default=datetime.datetime(2023, 5, 2, 6, 33, 26, 635193, tzinfo=utc), max_length=10),
            preserve_default=False,
        ),
    ]
