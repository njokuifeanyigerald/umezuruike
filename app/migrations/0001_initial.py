# Generated by Django 3.2.7 on 2021-10-12 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=10000)),
                ('last_name', models.CharField(max_length=10000)),
                ('email', models.CharField(max_length=10000)),
                ('phone', models.CharField(max_length=10000)),
                ('request', models.TextField(blank=True)),
                ('sent_date', models.DateTimeField(auto_now_add=True)),
                ('accepted', models.BooleanField(default=False)),
                ('accepted_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'appointments',
                'ordering': ['-sent_date'],
            },
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('name', models.CharField(max_length=500)),
                ('honor', models.CharField(blank=True, max_length=300, null=True)),
                ('job_title', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'personnels',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('title', models.CharField(max_length=500)),
                ('days_of_activities', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'services',
            },
        ),
    ]
