# Generated by Django 4.0.5 on 2022-06-07 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_game_max_playtime'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='trendinggame',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]