# Generated by Django 2.1.7 on 2019-02-22 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190222_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='budget_left',
            field=models.IntegerField(blank=True, help_text='This field will be assigned automatically', null=True),
        ),
    ]