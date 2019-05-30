# Generated by Django 2.2.1 on 2019-05-30 20:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_profile_creditcard'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField(null=True)),
                ('end_date', models.DateTimeField(null=True)),
                ('start_amount', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(1000000000), django.core.validators.MinValueValidator(1)])),
                ('description', models.TextField(max_length=500)),
                ('picture', models.TextField(null=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bid', to='accounts.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=500)),
                ('rating', models.IntegerField(validators=[django.core.validators.MaxValueValidator(9), django.core.validators.MinValueValidator(0)])),
                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='auction.Bid')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='accounts.Profile')),
            ],
        ),
    ]
