# Generated by Django 2.0.4 on 2018-11-19 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='aboutme',
            field=models.TextField(blank=True, default='无', null=True, verbose_name='自我介绍'),
        ),
    ]
