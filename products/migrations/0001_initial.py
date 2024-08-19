# Generated by Django 5.0.7 on 2024-08-12 14:52

import django.db.models.deletion  # Third-party imports
from django.db import migrations, models  # Django imports

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        # This is the initial migration, so no dependencies are needed.
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                # AutoField for primary key ID
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                # Name of the collection
                ('name', models.CharField(max_length=254)),
                # Friendly name (optional)
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                # AutoField for primary key ID
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                # SKU, which can be nullable and optional in forms
                ('sku', models.CharField(blank=True, max_length=254, null=True)),
                # Name of the product
                ('name', models.CharField(max_length=254)),
                # Description of the product
                ('description', models.TextField()),
                # Price with two decimal places, max digits 6
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                # Rating, which can be nullable and optional in forms
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                # Image URL, which can be nullable and optional in forms
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                # Image field, which can be nullable and optional in forms
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                # ForeignKey to Collection with SET_NULL on deletion
                ('collection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.collection')),
            ],
        ),
    ]
