# Generated by Django 2.0.3 on 2018-05-25 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailylog',
            name='category',
            field=models.CharField(choices=[('FOOD', 'food'), ('MUSIC', 'music'), ('PROGRAMMING', 'programming')], default='PROGRAMMING', max_length=15),
        ),
    ]
