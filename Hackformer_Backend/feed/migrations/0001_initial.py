# Generated by Django 4.1.7 on 2023-03-17 13:32

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('phone', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=15)),
                ('college', models.TextField()),
                ('college_city', models.CharField(max_length=100)),
                ('current_year', models.CharField(max_length=15)),
                ('branch', models.CharField(max_length=100)),
                ('about_me', models.TextField()),
                ('skills', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), size=None)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
