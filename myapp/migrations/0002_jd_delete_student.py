# Generated by Django 5.0.2 on 2024-02-17 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=20000)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
