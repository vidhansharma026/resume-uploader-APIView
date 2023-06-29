# Generated by Django 4.2 on 2023-06-27 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('state', models.CharField(choices=[('Bihar', 'Bihar'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Rajasthan', 'Rajasthan')], max_length=50)),
                ('gender', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('docs', models.FileField(blank=True, upload_to='documents')),
            ],
        ),
    ]