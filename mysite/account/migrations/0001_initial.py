# Generated by Django 3.2 on 2022-03-21 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10, unique=True)),
                ('password', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=64, unique=True)),
                ('mobile', models.CharField(default=None, max_length=32)),
                ('sex', models.CharField(default=0, max_length=10)),
                ('status', models.SmallIntegerField(choices=[(1, 'active'), (0, 'frozen')], default=1)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('user_id',),
            },
        ),
    ]
