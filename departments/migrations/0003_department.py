# Generated by Django 5.0.6 on 2024-06-23 19:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('departments', '0002_alter_planning_top_management'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='')),
                ('object_id', models.PositiveIntegerField()),
                ('slug', models.SlugField(editable=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('content_type', models.ForeignKey(limit_choices_to={'model__in': ('state', 'locality', 'unity')}, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('management', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department_related', to='departments.department', verbose_name='')),
            ],
            options={
                'verbose_name_plural': 'الإدارات التخطيطية',
                'ordering': ['created'],
            },
        ),
    ]
