# Generated by Django 4.2.11 on 2024-04-24 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_movie_release_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_poster',
            field=models.CharField(default='johnbean36', max_length=100),
            preserve_default=False,
        ),
    ]
