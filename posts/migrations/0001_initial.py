# Generated by Django 3.2.5 on 2021-08-16 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('passsword', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=45)),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
