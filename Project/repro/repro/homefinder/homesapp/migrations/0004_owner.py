# Generated by Django 2.1.3 on 2018-11-25 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homesapp', '0003_auto_20181113_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=200)),
                ('owner_phone_no', models.CharField(max_length=200)),
                ('owner_email_id', models.CharField(max_length=200)),
                ('property_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homesapp.Property')),
            ],
        ),
    ]
