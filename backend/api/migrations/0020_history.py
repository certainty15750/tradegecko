# Generated by Django 2.1.3 on 2019-03-04 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0019_customer_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(blank=True, default='', max_length=400)),
                ('browser_info', models.CharField(blank=True, default='', max_length=400)),
                ('location', models.CharField(blank=True, default='', max_length=400)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'history',
            },
        ),
    ]