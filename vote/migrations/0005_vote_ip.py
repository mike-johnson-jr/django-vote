# Generated by Django 2.1.5 on 2019-04-13 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0004_auto_20170110_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='ip',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]
