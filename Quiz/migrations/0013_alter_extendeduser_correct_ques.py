# Generated by Django 3.2.6 on 2021-12-30 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0012_auto_20211230_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendeduser',
            name='correct_ques',
            field=models.IntegerField(default=0),
        ),
    ]