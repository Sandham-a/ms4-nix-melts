# Generated by Django 5.0.7 on 2024-08-19 13:08

import django.db.models.deletion  # Third-party imports
from django.db import migrations, models  # Local imports


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_alter_order_country'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user_profile',
            field=models.ForeignKey(
                blank=True, 
                null=True, 
                on_delete=django.db.models.deletion.SET_NULL, 
                related_name='orders', 
                to='profiles.userprofile'
            ),
            # Adds an optional foreign key to UserProfile, allowing null values.
        ),
    ]
