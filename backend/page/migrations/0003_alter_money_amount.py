# Generated by Django 5.0 on 2024-01-03 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_remove_money_user_remove_user_name_user_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='money',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
