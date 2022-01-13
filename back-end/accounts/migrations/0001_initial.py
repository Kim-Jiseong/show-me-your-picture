# Generated by Django 3.2.11 on 2022-01-13 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('nickname', models.CharField(blank=True, max_length=20)),
                ('description', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]