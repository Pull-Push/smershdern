# Generated by Django 5.0.6 on 2024-06-19 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whiskeywheel', '0004_ww_member_member_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PersonClass',
        ),
        migrations.DeleteModel(
            name='TestClass',
        ),
        migrations.DeleteModel(
            name='ww_member',
        ),
    ]
