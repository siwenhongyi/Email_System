# Generated by Django 3.0.3 on 2020-02-17 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='friendlist',
            fields=[
                ('user_email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('friendemail', models.CharField(max_length=2000)),
            ],
            options={
                'db_table': 'friendlist',
            },
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('user_email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=16)),
                ('logon_time', models.DateField(auto_now=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('user_sex', models.NullBooleanField()),
                ('user_profile', models.CharField(max_length=100)),
                ('user_qq', models.IntegerField(null=True)),
                ('user_phonenum', models.IntegerField(null=True)),
                ('user_head', models.ImageField(blank=True, null=True, upload_to='app/static/media')),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=20)),
                ('content', models.CharField(max_length=1000)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('sendto', models.EmailField(max_length=254)),
                ('_from', models.EmailField(max_length=254)),
                ('isdelete', models.BooleanField(default=False)),
                ('user_email', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.user')),
            ],
            options={
                'db_table': 'mail',
                'ordering': ['time'],
            },
        ),
    ]
