# Generated by Django 4.0.6 on 2022-07-05 05:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0007_delete_poll'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.TextField()),
                ('options_one', models.CharField(max_length=120)),
                ('options_two', models.CharField(max_length=120)),
                ('options_three', models.CharField(max_length=120)),
                ('options_four', models.CharField(max_length=120)),
                ('counting_for_opt_one', models.IntegerField(default=0)),
                ('counting_for_opt_two', models.IntegerField(default=0)),
                ('counting_for_opt_three', models.IntegerField(default=0)),
                ('counting_for_opt_four', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]