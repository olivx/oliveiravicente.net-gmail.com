# Generated by Django 3.0.4 on 2020-03-22 23:26

from django.db import migrations, models

import account.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('nome', models.CharField(blank=True, max_length=30, verbose_name='nome')),
                ('is_admin', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=account.models.image_upload_to, verbose_name='Foto')),
                ('rua', models.CharField(blank=True, max_length=250, verbose_name='rua')),
                ('cidade', models.CharField(blank=True, max_length=250, verbose_name='cidade')),
                ('bairro', models.CharField(blank=True, max_length=250, verbose_name='bairro')),
                ('estado', models.CharField(blank=True, max_length=250, verbose_name='estado')),
                ('cep', models.CharField(blank=True, max_length=10, verbose_name='cep')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Cliente',
            },
            managers=[
                ('objects', account.models.UserManager()),
            ],
        ),
    ]
