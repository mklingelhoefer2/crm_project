# Generated by Django 4.2.3 on 2023-07-20 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='life_cycle_stage',
            field=models.CharField(default='Lead', max_length=20),
        ),
    ]