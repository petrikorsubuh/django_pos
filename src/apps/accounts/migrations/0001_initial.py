# Generated by Django 3.1.7 on 2021-04-08 15:38

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
            name='CardMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('create_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('nik_numb', models.IntegerField()),
                ('ktp_image', models.ImageField(upload_to='ktp/')),
                ('create_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=1)),
                ('photo', models.ImageField(upload_to='profile/')),
                ('create_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True, null=True)),
                ('card_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card', to='accounts.cardmembers')),
                ('customers', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
