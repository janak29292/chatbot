# Generated by Django 3.2.5 on 2021-08-01 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0005_query_intent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='opions',
        ),
        migrations.AddField(
            model_name='response',
            name='options',
            field=models.ManyToManyField(blank=True, null=True, to='chatapp.Option'),
        ),
        migrations.AlterUniqueTogether(
            name='query',
            unique_together={('intent', 'query', 'state', 'option')},
        ),
    ]
