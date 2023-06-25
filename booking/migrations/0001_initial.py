# Generated by Django 4.2.2 on 2023-06-25 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('table_time_limit', models.PositiveIntegerField()),
                ('phone_number', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=32)),
            ],
        ),
    ]