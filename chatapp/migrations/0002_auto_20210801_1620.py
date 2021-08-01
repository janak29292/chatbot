# Generated by Django 3.2.5 on 2021-08-01 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='query',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='chatapp.response'),
        ),
        migrations.AlterField(
            model_name='query',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paths', to='chatapp.state'),
        ),
    ]
