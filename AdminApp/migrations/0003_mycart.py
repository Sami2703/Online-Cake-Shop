# Generated by Django 4.0.1 on 2022-02-04 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0002_userinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('cake', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.cake')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.userinfo')),
            ],
            options={
                'db_table': 'MyCart',
            },
        ),
    ]
