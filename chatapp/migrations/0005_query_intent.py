# Generated by Django 3.2.5 on 2021-08-01 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0004_auto_20210801_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='intent',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='chatapp.intent'),
            preserve_default=False,
        ),
    ]
