# Generated by Django 3.1.7 on 2021-04-14 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='No Title property', max_length=500)),
                ('location', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('contact_num', models.CharField(max_length=10)),
                ('Price', models.IntegerField(default=1)),
                ('Type', models.CharField(max_length=30)),
                ('sale_type', models.CharField(choices=[('Rent', 'Rent'), ('Sale', 'Sale'), ('Lease', 'Lease')], default='Rent', max_length=30)),
                ('posted_on', models.DateTimeField(auto_now=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('title_slug', models.SlugField(default=' ')),
                ('Img', models.ImageField(default=None, upload_to='images/')),
                ('Name', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='property', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
