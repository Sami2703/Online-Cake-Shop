# Generated by Django 4.0.1 on 2022-02-07 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0003_mycart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardNo', models.CharField(max_length=4)),
                ('cvv', models.CharField(max_length=4)),
                ('expiry', models.CharField(max_length=8)),
                ('balance', models.FloatField(default=10000)),
            ],
            options={
                'db_table': 'Accounts',
            },
        ),
    ]
