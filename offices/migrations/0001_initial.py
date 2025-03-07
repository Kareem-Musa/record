# Generated by Django 5.0.6 on 2024-08-13 13:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0009_alter_city_locality_alter_city_name_alter_city_state_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hquarter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='')),
                ('slug', models.SlugField(editable=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='state', to='locations.state', verbose_name='')),
            ],
            options={
                'verbose_name_plural': 'الرئاسات',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='')),
                ('slug', models.SlugField(editable=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('hquarter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hquarter_sectors', to='offices.hquarter', verbose_name='')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='state_sectors', to='locations.state', verbose_name='')),
            ],
            options={
                'verbose_name_plural': 'القطاعات',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='')),
                ('slug', models.SlugField(editable=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('hquarter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hquarter_offices', to='offices.hquarter', verbose_name='')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='state_offices', to='locations.state', verbose_name='')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sector_offices', to='offices.sector', verbose_name='')),
            ],
            options={
                'verbose_name_plural': 'المكاتب',
                'ordering': ['created'],
            },
        ),
    ]
