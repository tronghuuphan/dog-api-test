# Generated by Django 3.2.8 on 2021-10-31 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0002_alter_dog_breed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
    ]