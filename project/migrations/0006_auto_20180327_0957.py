# Generated by Django 2.0.3 on 2018-03-27 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20180327_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='employee',
            field=models.ManyToManyField(blank=True, null=True, to='index.Profile'),
        ),
    ]
