# Generated by Django 3.0.8 on 2020-08-04 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birdie_app', '0008_auto_20200803_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birdie',
            name='course',
            field=models.CharField(blank=True, choices=[('Broadmoor', 'Broadmoor'), ('Camas Meadows', 'Camas Meadows'), ('Colwood', 'Colwood'), ('Heron Lakes Great Blue', 'Heron Lakes Great Blue'), ('Heron Lakes Greenback', 'Heron Lakes Greenback'), ('Lewis River', 'Lewis River'), ('Tri Mountain', 'Tri Mountain')], max_length=100, null=True),
        ),
    ]
