# Generated by Django 3.2.5 on 2021-08-16 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('passsword', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=45)),
                ('country', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=50)),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='users',
        ),
    ]
