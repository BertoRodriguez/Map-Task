# Generated by Django 4.1.7 on 2023-05-13 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_game_finishedmaps_game_finishedfollowerurl_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condition',
            name='game_type',
            field=models.CharField(choices=[('MT', 'Map Task')], default='MT', max_length=2),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_type',
            field=models.CharField(choices=[('MT', 'Map Task')], default='MT', max_length=2),
        ),
    ]
